#Количество строк
"""Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет общее количество строк кода, игнорируя пустые строки и строчки комментариев."""

import os
#путь к нужной директории
target_dir = r"C:\Root\RemoteFolders\user0907"
search_path = os.path.join(target_dir, 'python-ds', 'setters and getters')
output_file = os.path.join(search_path, '02-Karma')

#функция для поиска в конкретном пути
def gen_files(target_path, search_directory):
    #проверка существования пути в файловой системе и проверка на директорию
    if os.path.exists(target_path) and os.path.isdir(target_path):
        print(f"Каталог: {target_path}")
        processed = set()  #набор для уже обработанных путей
        #обходим директории с помощью стека
        stack = [target_path]  #начинаем с целевого пути
        while stack:
            current_dir = stack.pop()  #берем последнюю директорию из стека
            try:
                #попытка открыть директорию и вернуть итератор
                with os.scandir(current_dir) as entries:
                    #перебираем все элементы в директории
                    for entry in entries:
                        #проверка на уже обработанную директорию
                        if entry.path in processed:
                            continue
                        processed.add(entry.path)
                        #если элемент является файлом - открываем и считаем символы
                        if entry.is_file():
                            try:
                                with open(entry.path, 'r', encoding='utf-8') as file_with:
                                    line_count = 0
                                    char_count = 0
                                    #читаем файл построчно
                                    for line in file_with:
                                        if line.strip():  #если строка не пустая
                                            line_count += 1
                                            char_count += len(line)
                                    #yield возвращает кортеж (путь_к_файлу, количество_символов)
                                    yield (entry.path, line_count, char_count)
                            except (UnicodeDecodeError, PermissionError) as e:
                                print(f"Ошибка чтения файла {entry.path}: {e}")
                                #в случае отсутсвия символов в файле возращаем тоже кортеж из пути и нуля строк и символов
                                yield (entry.path, 0, 0)
                        #если это директория - добавляем в стек
                        elif entry.is_dir():
                            stack.append(entry.path)
            except PermissionError:
                print(f"Нет доступа к: {current_dir}")
                continue
    else:
        print(f"Каталог {target_path} не найден или не является директорией")
#запускаем функцию
for file_info in gen_files(output_file, target_dir):
    file_path, line_count, char_count = file_info  #распаковываем кортеж
    print(f"Файл: {file_path}, Строк: {line_count}, Символов: {char_count}")
