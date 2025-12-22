# config.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'
INPUT_DIR = DATA_DIR / 'input'
ARCHIVE_DIR = DATA_DIR / 'archive'
CACHE_DIR = DATA_DIR / 'cache'

NETWORK_SHARE_PATH = r'\\vra.local\Root\Public\ОИС\Системы отчетности и анализа данных\Производительность\ПДЗ\архив'

JSON_SEARCH_PATHS = [
    str(INPUT_DIR),
    NETWORK_SHARE_PATH,
    str(CACHE_DIR),
]

# ИСПРАВЛЕННЫЙ DB_CONFIG:
DB_CONFIG = {
    'drivername': 'mssql+pyodbc',
    'host': 'db23',                 # СЕРВЕР
    'database': 'витринаданных',    # БАЗА ДАННЫХ
    'driver': 'SQL Server',         # Тот драйвер
    'trusted_connection': 'yes'
}


TARGET_TABLE = 'plan-fakt-otgruzok'