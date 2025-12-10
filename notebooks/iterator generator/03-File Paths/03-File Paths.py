#Пути файлов
"""Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов.

Решение задачи должно быть без рекурсии."""
import os
#путь к нужной директории
target_dir = r"C:\Root\RemoteFolders\user0907"
search_path = os.path.join(target_dir, 'python-ds', 'setters and getters')
output_file = os.path.join(search_path, '02-Karma')
#функция для посика в конкретном пути
def gen_files(target_path, search_directory):
    #проверка существования пути в файловой системе и проверка на директорию
    if os.path.exists(target_path) and os.path.isdir(target_path):
        print(f"Каталог: {target_path}")
        #обходим директории с помощью стека
        stack = [target_path]  #начинаем с целевого пути
        while stack:
            current_dir = stack.pop()  #берем последнюю директорию из стека
            try:
                #попытка открыть директорию и вернуть итератор
                with os.scandir(current_dir) as entries:
                    #перебираем все элементы в директории
                    for entry in entries:
                        #если элемент является файлом - возвращаем путь к этому файлу, как элемент генератора
                        if entry.is_file():
                            yield entry.path
                        #если это директория - добавляем в стек
                        elif entry.is_dir():
                            stack.append(entry.path)
            except PermissionError:
                print(f"Нет доступа к: {current_dir}")
                continue
#запускаем функцию
for file_path in gen_files(output_file, target_dir):
    print(file_path)