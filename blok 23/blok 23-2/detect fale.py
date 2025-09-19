#Поиск файла
import os

print(f"Название файла: {'main.py'}")
print(f"Стартовая диерктория: {os.path.abspath(os.path.join('..','..', '18_List_comprehensions'))}")

def find_file(cur_path, file_name):
    found_files =[]
    #в текущей директории создаем пути для каджого элемента
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)

        #если нашли файл в директории и это является файлом, добавляем найденный путь в список
        if os.path.isfile(path) and i == file_name:
            found_files.append(path)  # Добавляем найденный файл

        #если файла нет (это директория), создаем рекурсию для поиска во вложенных диреториях
        elif os.path.isdir(path):
            found_files.extend(find_file(path, file_name))  # Рекурсивный поиск в поддиректориях
    #функция возвращает список путей к искомым файлам
    return found_files
#в список путей к каждому элементу добавляем искомый файл
file_path = find_file(os.path.abspath(os.path.join('..','..', '18_List_comprehensions')), 'main.py')
#проходим циклом по списку и выводим элемены этого списка
if file_path:
    print("\nНайдены следующие файлы 'main.py':")
    for i, path in enumerate(file_path, 1):
        print(f"{i}. {path}")

else:
    print('файл не найден')

