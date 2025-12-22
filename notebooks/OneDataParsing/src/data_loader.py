# src/data_loader.py
import pandas as pd
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class UniversalJsonLoader:
    """Универсальный загрузчик JSON файлов"""

    def load_json(self, file_path: str):
        try:
            # В Jupyter используем pd.read_json - делаем так же здесь
            df_s = pd.read_json(file_path)

            # Отладка
            logger.debug(f"DataFrame shape после pd.read_json: {df_s.shape}")
            logger.debug(f"DataFrame колонки: {df_s.columns.tolist()}")
            logger.debug(f"Первые 2 строки:\n{df_s.head(2)}")

            # Проверяем, что DataFrame имеет нужную структуру 1С
            if len(df_s) >= 2 and '#type' in df_s.columns and '#value' in df_s.columns:
                logger.info("Обнаружена структура 1С ValueTable, парсим...")
                return self._parse_1c_value_table(df_s)
            elif len(df_s) > 0:
                logger.info("Это обычный JSON, возвращаем как есть")
                return df_s
            else:
                logger.warning("DataFrame пуст")
                return pd.DataFrame()

        except Exception as e:
            logger.error(f"Ошибка загрузки файла {file_path}: {e}", exc_info=True)
            return None

    def _parse_1c_value_table(self, df_s: pd.DataFrame) -> pd.DataFrame:
        """Парсит структуру 1С ValueTable из DataFrame"""
        try:
            # Извлекаем метаданные столбцов из первой строки
            if len(df_s) < 2:
                logger.error("Недостаточно строк для парсинга 1С формата")
                return pd.DataFrame()

            # Первая строка содержит метаданные колонок
            first_row = df_s.iloc[0]
            column_metadata = first_row['#value'] if isinstance(first_row['#value'], list) else []

            # Вторая строка содержит данные
            second_row = df_s.iloc[1]
            table_data = second_row['#value'] if isinstance(second_row['#value'], list) else []

            # Проверяем данные
            if not column_metadata or not table_data:
                logger.warning("Нет метаданных колонок или данных для парсинга")
                return pd.DataFrame()

            # Извлекаем имена колонок
            column_names = []
            for col_meta in column_metadata:
                if isinstance(col_meta, dict):
                    name = col_meta.get('Name', {})
                    if isinstance(name, dict) and '#value' in name:
                        column_names.append(name['#value'])
                    else:
                        title = col_meta.get('Title', f"col_{len(column_names)}")
                        column_names.append(title)
                else:
                    column_names.append(f"col_{len(column_names)}")

            logger.debug(f"Найдены колонки: {column_names}")

            # Преобразуем данные в строки
            parsed_rows = []
            for row in table_data:
                if isinstance(row, list):
                    row_dict = {}
                    for col_idx, cell in enumerate(row):
                        col_name = column_names[col_idx] if col_idx < len(column_names) else f"extra_col_{col_idx}"

                        # Извлекаем значение из структуры 1С
                        if isinstance(cell, dict) and '#value' in cell:
                            row_dict[col_name] = cell['#value']
                        else:
                            row_dict[col_name] = cell
                    parsed_rows.append(row_dict)

            result_df = pd.DataFrame(parsed_rows)
            logger.info(f"Успешно распаршено {len(result_df)} строк, {len(result_df.columns)} колонок")
            return result_df

        except Exception as e:
            logger.error(f"Ошибка парсинга 1С формата: {e}", exc_info=True)
            return pd.DataFrame()

    def _parse_flat_json(self, raw_data) -> pd.DataFrame:
        """Парсит плоский JSON"""
        try:
            if isinstance(raw_data, list):
                return pd.DataFrame(raw_data)
            elif isinstance(raw_data, dict):
                return pd.DataFrame([raw_data])
            return pd.DataFrame()
        except Exception as e:
            logger.error(f"Ошибка парсинга плоского JSON: {e}")
            return pd.DataFrame()