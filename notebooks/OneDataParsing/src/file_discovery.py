# src/file_discovery.py
import os
import glob
import shutil
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict

logger = logging.getLogger(__name__)

class FileDiscoverer:
    """Класс для поиска файлов (упрощенная версия без win32)"""

    def __init__(self, processed_log_path: str = None):
        """
        Args:
            processed_log_path: путь к файлу лога обработанных файлов
        """
        self.found_files = []

        # Путь к файлу лога обработанных файлов
        if processed_log_path:
            self.processed_log_path = Path(processed_log_path)
        else:
            # По умолчанию в корне проекта
            self.processed_log_path = Path(__file__).parent.parent / "processed_files.json"

        # Загружаем список уже обработанных файлов
        self.processed_files = self._load_processed_files()
        logger.info(f"Загружено {len(self.processed_files)} обработанных файлов из лога")

    def _load_processed_files(self) -> set:
        """Загружает список уже обработанных файлов"""
        try:
            if self.processed_log_path.exists():
                with open(self.processed_log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return set(data)
            return set()
        except Exception as e:
            logger.warning(f"Не удалось загрузить лог обработанных файлов: {e}")
            return set()

    def _save_processed_files(self):
        """Сохраняет список обработанных файлов"""
        try:
            with open(self.processed_log_path, 'w', encoding='utf-8') as f:
                json.dump(list(self.processed_files), f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Не удалось сохранить лог обработанных файлов: {e}")

    def discover_json_files(self, search_paths: List[str]) -> List[Dict]:
        """
        Ищет все JSON файлы в указанных путях, исключая уже обработанные

        Args:
            search_paths: список путей для поиска

        Returns:
            Список словарей с информацией о файлах
        """
        all_files = []

        for search_path in search_paths:
            # Пропускаем недоступные пути
            if not self._path_exists(search_path):
                logger.warning(f"Путь недоступен: {search_path}")
                continue

            # Ищем файлы
            files = self._find_files_in_path(search_path)

            # Фильтруем уже обработанные файлы
            for file_info in files:
                full_path = file_info['full_path']

                # Пропускаем если уже обрабатывали
                if full_path in self.processed_files:
                    logger.debug(f"Пропускаем уже обработанный файл: {file_info['filename']}")
                    continue

                # Пропускаем файлы из архива (они уже обработаны ранее)
                if "archive" in full_path.lower():
                    logger.debug(f"Пропускаем архивный файл: {file_info['filename']}")
                    self.mark_as_processed(full_path)  # Помечаем как обработанный
                    continue

                all_files.append(file_info)

        logger.info(f"Найдено {len(all_files)} новых JSON файлов (исключая {len(self.processed_files)} уже обработанных)")
        self.found_files = all_files
        return all_files

    def mark_as_processed(self, file_path: str):
        """
        Помечает файл как обработанный

        Args:
            file_path: полный путь к обработанному файлу
        """
        try:
            self.processed_files.add(file_path)
            self._save_processed_files()
            logger.debug(f"Файл помечен как обработанный: {file_path}")
        except Exception as e:
            logger.error(f"Не удалось пометить файл как обработанный: {e}")

    def _path_exists(self, path: str) -> bool:
        """Проверяет доступность пути"""
        try:
            return os.path.exists(path)
        except Exception as e:
            logger.debug(f"Путь {path} недоступен: {e}")
            return False

    def _find_files_in_path(self, path: str) -> List[Dict]:
        """Ищет файлы в указанном пути"""
        files = []

        # Ищем все JSON файлы
        pattern = os.path.join(path, '**', '*.json')

        try:
            found = glob.glob(pattern, recursive=True)

            for file_path in found:
                if os.path.isfile(file_path):
                    file_info = {
                        'full_path': file_path,
                        'filename': os.path.basename(file_path),
                        'directory': os.path.dirname(file_path),
                        'size': os.path.getsize(file_path),
                        'modified': datetime.fromtimestamp(os.path.getmtime(file_path)),
                        'is_network': file_path.startswith(r'\\')
                    }
                    files.append(file_info)

        except Exception as e:
            logger.error(f"Ошибка поиска в {path}: {e}")

        return files

    def copy_to_local_cache(self, file_info: Dict, cache_dir: str) -> str:
        """
        Копирует файл в локальный кэш для обработки
        """
        os.makedirs(cache_dir, exist_ok=True)

        # Генерируем уникальное имя
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        local_filename = f"{timestamp}_{file_info['filename']}"
        local_path = os.path.join(cache_dir, local_filename)

        try:
            shutil.copy2(file_info['full_path'], local_path)
            logger.info(f"Файл скопирован в кэш: {local_path}")
            return local_path
        except Exception as e:
            logger.error(f"Ошибка копирования файла: {e}")
            # В случае ошибки возвращаем оригинальный путь
            return file_info['full_path']