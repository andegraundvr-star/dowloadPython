# src/database_handler.py
import pandas as pd
import logging
from sqlalchemy import create_engine, text, MetaData, Table, Column
from sqlalchemy.types import NVARCHAR, DATETIME, INTEGER, DECIMAL
import urllib.parse

logger = logging.getLogger(__name__)

class DatabaseHandler:
    """Обработчик для MSSQL - упрощенная версия"""

    def __init__(self, db_config: dict, table_name: str):
        self.db_config = db_config
        self.table_name = table_name  # 'plan-fakt-otgruzok'
        self.schema = 'dbo'
        self.engine = None

    def connect(self) -> bool:
        """Подключается к MSSQL"""
        try:
            host = self.db_config.get('host', 'db23')
            database = self.db_config.get('database', 'витринаданных')
            driver = self.db_config.get('driver', 'SQL Server')

            connection_string = (
                f"mssql+pyodbc://{host}/{database}?"
                f"trusted_connection=yes&"
                f"driver={urllib.parse.quote_plus(driver)}"
            )

            self.engine = create_engine(connection_string)

            with self.engine.connect() as conn:
                logger.info(f"✅ Подключение успешно: {host}/{database}")
                return True

        except Exception as e:
            logger.error(f"❌ Ошибка подключения: {e}")
            return False

    def append_data(self, df: pd.DataFrame) -> bool:
        """Добавляет данные в существующую таблицу"""
        try:
            if df.empty:
                logger.warning("DataFrame пуст")
                return False

            # 1. Убедимся, что таблица существует
            if not self._table_exists():
                logger.error(f"Таблица [{self.schema}].[{self.table_name}] не существует!")
                return False

            # 2. Проверяем структуру таблицы
            table_columns = self._get_table_columns()
            df_columns = df.columns.tolist()

            # Проверяем соответствие колонок
            missing_in_table = set(df_columns) - set(table_columns)
            missing_in_df = set(table_columns) - set(df_columns)

            if missing_in_table:
                logger.error(f"В таблице отсутствуют колонки: {missing_in_table}")
                return False

            if missing_in_df:
                logger.warning(f"В DataFrame отсутствуют колонки таблицы: {missing_in_df}")

            # 3. Вставляем данные через безопасный метод
            inserted = self._safe_insert_data(df, table_columns)

            if inserted:
                logger.info(f"✅ Добавлено {len(df)} записей в [{self.schema}].[{self.table_name}]")
            return inserted

        except Exception as e:
            logger.error(f"❌ Ошибка записи: {e}", exc_info=True)
            return False

    def _table_exists(self) -> bool:
        """Проверяет существование таблицы"""
        try:
            # Простой запрос без CAST для NVARCHAR(max)
            query = f"""
            SELECT 1 
            FROM sys.tables t
            JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE s.name = '{self.schema}' 
              AND t.name = '{self.table_name}'
            """

            with self.engine.connect() as conn:
                result = conn.execute(text(query)).fetchone()
                exists = result is not None
                logger.debug(f"Таблица существует: {exists}")
                return exists

        except Exception as e:
            logger.error(f"Ошибка проверки таблицы: {e}")
            return False

    def _get_table_columns(self) -> list:
        """Получает список колонок таблицы"""
        try:
            query = f"""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{self.schema}'
              AND TABLE_NAME = '{self.table_name}'
            ORDER BY ORDINAL_POSITION
            """

            with self.engine.connect() as conn:
                result = conn.execute(text(query)).fetchall()
                columns = [row[0] for row in result]
                logger.debug(f"Колонки таблицы: {columns}")
                return columns

        except Exception as e:
            logger.error(f"Ошибка получения колонок: {e}")
            return []

    def _safe_insert_data(self, df: pd.DataFrame, table_columns: list) -> bool:
        """Безопасная вставка данных с учетом порядка колонок"""
        try:
            # Приводим порядок колонок DF к порядку в таблице
            df_columns = df.columns.tolist()

            # Оставляем только колонки, которые есть в таблице
            columns_to_insert = [col for col in table_columns if col in df_columns]

            if not columns_to_insert:
                logger.error("Нет совпадающих колонок для вставки!")
                return False

            # Формируем SQL для вставки
            col_names = ', '.join([f"[{col}]" for col in columns_to_insert])
            # Используем именованные параметры для SQLAlchemy
            param_names = ', '.join([f":{col}" for col in columns_to_insert])

            insert_sql = f"""
            INSERT INTO [{self.schema}].[{self.table_name}] ({col_names})
            VALUES ({param_names})
            """

            # Подготавливаем данные как список словарей
            data_to_insert = []
            for _, row in df.iterrows():
                row_dict = {}
                for col in columns_to_insert:
                    val = row[col]
                    # Обработка NULL значений
                    if pd.isna(val):
                        row_dict[col] = None
                    else:
                        # Конвертируем типы если нужно
                        if isinstance(val, pd.Timestamp):
                            row_dict[col] = val.to_pydatetime()
                        else:
                            row_dict[col] = val
                data_to_insert.append(row_dict)

            # Вставляем пачками
            batch_size = 100
            with self.engine.connect() as conn:
                for i in range(0, len(data_to_insert), batch_size):
                    batch = data_to_insert[i:i + batch_size]
                    conn.execute(text(insert_sql), batch)
                    conn.commit()
                    logger.debug(f"Вставлено {len(batch)} записей (пакет {i//batch_size + 1})")

            return True

        except Exception as e:
            logger.error(f"Ошибка вставки: {e}", exc_info=True)
            return False
    def close(self):
        if self.engine:
            self.engine.dispose()
            logger.info("Соединение закрыто")