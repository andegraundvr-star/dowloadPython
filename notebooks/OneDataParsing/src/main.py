# src/main.py
import os
import sys
import logging
import shutil
from datetime import datetime
from pathlib import Path

# Импорты из наших модулей
from .file_discovery import FileDiscoverer
from .data_loader import UniversalJsonLoader
from .database_handler import DatabaseHandler
from .config import (
    JSON_SEARCH_PATHS, CACHE_DIR, ARCHIVE_DIR,
    DB_CONFIG, TARGET_TABLE
)

def setup_logging():
    """Настройка логирования"""
    from .config import LOGS_DIR

    # Создаем директорию для логов (если её еще нет)
    LOGS_DIR.mkdir(exist_ok=True)

    # Создаем уникальное имя для файла лога с датой
    log_filename = f"etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_filepath = LOGS_DIR / log_filename

    # Настройка формата логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # 1. Запись в файл
            logging.FileHandler(log_filepath, encoding='utf-8', mode='w'),
            # 2. Вывод в консоль
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Логирование настроено. Файл лога: {log_filepath}")
    return logger

def process_single_file(file_path: str, loader: UniversalJsonLoader,
                        db_handler: DatabaseHandler, cache_dir: str) -> bool:
    """Обрабатывает один файл"""
    logger = logging.getLogger(__name__)

    try:
        # Загружаем и парсим данные
        df = loader.load_json(file_path)

        if df is None or df.empty:
            logger.warning(f"Файл не содержит данных: {file_path}")
            return False

        # Загружаем в базу данных
        success = db_handler.append_data(df)

        if success:
            logger.info(f"✅ Успешно обработан: {os.path.basename(file_path)} ({len(df)} записей)")
            return True
        else:
            logger.error(f"❌ Ошибка БД: {os.path.basename(file_path)}")
            return False

    except Exception as e:
        logger.error(f"❌ Ошибка обработки файла: {e}")
        return False

def archive_file(file_path: str, archive_base: str):
    """Перемещает файл в архив"""
    try:
        # Создаем структуру архива по дате
        archive_date = datetime.now().strftime('%Y/%m/%d')
        archive_path = os.path.join(archive_base, archive_date)
        os.makedirs(archive_path, exist_ok=True)

        # Новое имя файла
        timestamp = datetime.now().strftime('%H%M%S')
        filename = os.path.basename(file_path)
        archived_name = f"{timestamp}_{filename}"
        archived_path = os.path.join(archive_path, archived_name)

        # Перемещаем файл
        shutil.move(file_path, archived_path)
        logging.getLogger(__name__).info(f"Файл заархивирован: {archived_path}")

    except Exception as e:
        logging.getLogger(__name__).warning(f"Не удалось архивировать файл: {e}")

def main():
    """Основная функция ETL"""
    logger = setup_logging()

    logger.info("=" * 50)
    logger.info("Запуск ETL процесса")
    logger.info("=" * 50)

    # 1. Инициализация компонентов
    file_discoverer = FileDiscoverer()
    json_loader = UniversalJsonLoader()
    db_handler = DatabaseHandler(DB_CONFIG, TARGET_TABLE)

    # 2. Поиск файлов
    logger.info("Поиск JSON файлов...")
    file_infos = file_discoverer.discover_json_files(JSON_SEARCH_PATHS)

    if not file_infos:
        logger.info("Нет файлов для обработки")
        return True

    logger.info(f"Найдено {len(file_infos)} файлов")

    # 3. Подключение к БД
    if not db_handler.connect():
        logger.error("Не удалось подключиться к БД")
        return False

    # 4. Обработка файлов
    success_count = 0

    for i, file_info in enumerate(file_infos, 1):
        logger.info(f"[{i}/{len(file_infos)}] Обработка: {file_info['filename']}")

        # Для сетевых файлов копируем в кэш
        if file_info['is_network']:
            file_path = file_discoverer.copy_to_local_cache(file_info, str(CACHE_DIR))
        else:
            file_path = file_info['full_path']

        # Обрабатываем файл
        if process_single_file(file_path, json_loader, db_handler, str(CACHE_DIR)):
            success_count += 1

            # ПОМЕЧАЕМ ФАЙЛ КАК ОБРАБОТАННЫЙ
            file_discoverer.mark_as_processed(file_info['full_path'])

            # Архивируем успешно обработанный файл
            archive_file(file_info['full_path'], str(ARCHIVE_DIR))

    # 5. Отчет
    logger.info("=" * 50)
    logger.info(f"ИТОГО: Успешно {success_count}/{len(file_infos)} файлов")
    logger.info("=" * 50)

    db_handler.close()
    return success_count > 0

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        logging.error(f"Критическая ошибка: {e}", exc_info=True)
        sys.exit(1)