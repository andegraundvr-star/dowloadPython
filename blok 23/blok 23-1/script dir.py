#скрипт Dir

import os
import sys

def in_direct(project):
    print(f"\nСодержимое директории {project}")
    try:
        items = os.listdir(project)
        if not items:
            print("  [Директория пуста]")
        for item in items:
            print(f"  {os.path.join(project, item)}")
    except FileNotFoundError:
        print(f"  Ошибка: директория не найдена")
    except PermissionError:
        print(f"  Ошибка: нет доступа к директории")

# Основной абсолютный путь
python_basic = r"C:\Users\user0907\AppData\Local\Programs\Python\Python313\Scripts\venv\blok\blok 23 practicum"

# Альтернативный способ определения пути скрипта
try:
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    python_basic_dev = os.path.join(script_dir)
except:
    python_basic_dev = 'не работает'  # fallback

print(f"Production путь: {python_basic}")
print(f"Dev путь: {python_basic_dev}")

# Проверяем доступность путей

if os.path.exists(python_basic_dev):
    target_dir = python_basic_dev
    print("Используется dev путь")
elif os.path.exists(python_basic):
    target_dir = python_basic
    print("Используется production путь")
else:
    print("Оба пути недоступны!")
    sys.exit(1)

# Выводим содержимое
in_direct(target_dir)

print(f"[DEBUG] Текущая директория скрипта: {script_dir}")
print(f"[DEBUG] Dev путь: {python_basic_dev}")
print(f"[DEBUG] Существует: {os.path.exists(python_basic_dev)}")