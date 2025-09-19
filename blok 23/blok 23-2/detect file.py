import os
import sys

print(f"\nВведите имя папки: ")
object_name = 'by pairs.py'  # или input()
print(object_name)
def find_object(root_dir, target_name):
    """Рекурсивно ищет файл или папку по имени"""
    for root, dirs, files in os.walk(root_dir):
        if target_name in dirs:
            return os.path.join(root, target_name)
        if target_name in files:
            return os.path.join(root, target_name)
    return None

#получаем корень диска, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
drive = os.path.splitdrive(script_dir)[0] + os.sep  # Например: "C:\"

#ищем объект
file_path = find_object(drive, object_name)  # Правильный порядок аргументов
print(f"Найденный путь: {file_path}")

if file_path and os.path.exists(file_path):
    if os.path.isfile(file_path):
        print("Это файл")
    elif os.path.isdir(file_path):
        print("Это директория")
else:
    print("Указанного пути не существует")