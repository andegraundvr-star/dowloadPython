#Иконки
import os


print(f"\nВведите имя папки: ")

# Основной абсолютный путь

base_dir = r"C:\Root\RemoteFolders\user0907\python-ds\blok21\Tuples"
object_name = "by pairs.py"
print(object_name)
print(f"Путь: {os.path.join(base_dir,object_name)}")


full_path = os.path.join(base_dir, object_name)

if os.path.exists(full_path):
    if os.path.isfile(full_path):
        print(f"Это файл")
        # Получаем размер файла в байтах
        file_size = os.path.getsize(full_path)
        print(f"Размер файла: {file_size} байт")
    elif os.path.isdir(full_path):
        print(f"Это директория")
else:
    print("Указанного пути не существует")
    # Дополнительные проверки
    print("\nДиагностика:")
    print(f"Базовая директория существует: {os.path.exists(base_dir)}")
    if os.path.exists(base_dir):
        print(f"Содержимое {base_dir}:")
        try:
            print(os.listdir(base_dir))
        except PermissionError:
            print("Нет прав на чтение директории")







