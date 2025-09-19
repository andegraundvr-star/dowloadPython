#Поиск файла 2
import os
import random

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
count = 0
path_list = []
if file_path:
    print("\nНайдены следующие файлы 'main.py':")
    for i, path in enumerate(file_path, 1):
        #создаем спиоск путей к файлу и нумерацию путей
        count += 1
        path_list.append(path)
        print(f"{i}. {path}")


else:
    print('файл не найден')
#задаем пеерменную рандомного числа, для последующего прочтения файла в соответсвии с номером рандомной строчки
random_path = random.randint(1,count)
target_file = path_list[random_path - 1]
print(f"читаем рандомный файл: {random_path}. {path_list[random_path - 1]}")
print()
#открываем файл, проходим циклом по строкам файлов, закрываем файл
file = open(path_list[random_path - 1], 'r',encoding='utf-8')

for i_line in file:
    print(i_line, end = '')
file.close()
