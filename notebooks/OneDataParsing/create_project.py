# create_project.py
import os
from pathlib import Path

def create_structure():
    """Создает структуру проекта"""

    # Директории
    directories = [
        'data/input',
        'data/archive',
        'data/cache',
        'logs',
        'src',
    ]

    # Файлы
    files = {
        'requirements.txt': """pandas>=1.5.0
sqlalchemy>=2.0.0""",

        'src/__init__.py': '',
        'src/config.py': '''import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'
INPUT_DIR = DATA_DIR / 'input'
ARCHIVE_DIR = DATA_DIR / 'archive'
CACHE_DIR = DATA_DIR / 'cache'

NETWORK_SHARE_PATH = r'\\\\vra.local\\Root\\Public\\ОИС\\Системы отчетности и анализа данных\\Производительность\\ПДЗ\\архив'

JSON_SEARCH_PATHS = [
    str(INPUT_DIR),
    NETWORK_SHARE_PATH,
    str(CACHE_DIR),
]

DB_CONFIG = {
    'drivername': 'sqlite',
    'database': str(DATA_DIR / 'production.db'),
}

TARGET_TABLE = 'nomenklatura_movement'
''',
    }

    # Создаем директории
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Создана директория: {dir_path}")

    # Создаем файлы
    for file_path, content in files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Создан файл: {file_path}")

    print("\n✅ Проект создан!")
    print("\nСледующие шаги:")
    print("1. Поместите JSON файлы в папку data/input/")
    print("2. Установите зависимости: pip install -r requirements.txt")
    print("3. Запустите проект: python -m src.main")

if __name__ == "__main__":
    create_structure()