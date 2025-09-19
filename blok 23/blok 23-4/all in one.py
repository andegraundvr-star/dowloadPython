#Всё в одном
import os
#создание функции, которая создает пути ко всем файлам заданной диоектории, открывает их, считывает содержимое, записывает в отдельный файл и закрывает
def in_direct(project, output_file):
    print(f"\nСодержимое директории {project}")
    try:
        #открываем файл для записи всех данных один раз
        with open(output_file, 'w', encoding='utf-8') as all_in_one:
            for i_name in os.listdir(project):
                #записывем путь к файлу в переменную
                path = os.path.join(project, i_name)
                #пропускаем подкаталоги, работаем только с файлами
                if not os.path.isfile(path):
                    continue
                #отмечаем, какой файл копируем
                print(f"Обработка файла: {i_name}")
                try:
                    #открываем файл по вновь заданному пути
                    with open(path, 'r', encoding='utf-8') as file:
                        #читаем файл и запоминаем в переменную
                        content = file.read()

                        #записываем в общий файл
                        all_in_one.write(f"=== Содержимое файла {i_name} ===\n") #обозначаем обработку
                        all_in_one.write(content)
                        all_in_one.write("\n" + 40 * '*' + "\n") #добавляем разделительную строку
                #в противном случае записываем содержимое ошибки
                except UnicodeDecodeError:
                    print(f"  Ошибка: файл {i_name} не текстовый или имеет другую кодировку")
                except PermissionError:
                    print(f"  Ошибка: нет доступа к файлу {i_name}")

    except FileNotFoundError:
        print(f"  Ошибка: директория не найдена")


base_dir = r"C:\Root\RemoteFolders\user0907\python-ds"
python_basic = os.path.join(base_dir, 'blok16 trening1')
output_path = os.path.join(base_dir, 'all_files_content.txt')  #файл для результатов

#выбираем директорию и применяем функцию
#print(f"Содержимое каталога {python_basic}")
in_direct(python_basic, output_path)
print(f"\nРезультат сохранён в: {output_path}")

