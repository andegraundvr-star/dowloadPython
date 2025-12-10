import os


# Сохранение
line = 'hgkhsg'#input("Введите строку: ")
path_line = 'Root RemoteFolders user0907 python-ds 23_Files 05_save'#input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ")
file_name = 'hgkhsg'#input("Введите имя файла: ")
#создаем путь
path_parts = path_line.split()  #разбиваем строку по пробелам
correct_path = os.path.join(*path_parts) #собираем путь с разделителями
#print(correct_path)
#создаем полный путь к файлу
full_path = os.path.join('C:\\',correct_path, file_name + '.txt')
#print(full_path)

#сохраняем содержимое в файл
with open(full_path, 'w', encoding='utf-8') as file:
    file.write(line)
if os.path.exists(full_path):
    answer = input("Вы действительно хотите перезаписать файл? (y/n): ")
    if answer.lower() != 'y':
        print("Сохранение отменено")
        exit()

print(f"Файл успешно сохранен по пути: {full_path}")