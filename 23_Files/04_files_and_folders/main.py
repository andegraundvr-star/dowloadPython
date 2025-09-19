# Файлы и папки
import os


def analyze_directory(start_path):
    total_size = 0
    dir_count = 0
    file_count = 0
    #создаем цикл прохода по директории по заданному пути
    for item in os.listdir(start_path):
        #создаем путь
        path = os.path.join(start_path, item)
        #делаем проверку на файл или диркторию
        if os.path.isfile(path):
            #для файлов создаем посчет размера и количества
            file_count += 1
            total_size += os.path.getsize(path)

        elif os.path.isdir(path):
            #для директорий - создаем рекурсию с подсчетом требуемых значений
            dir_count += 1
            sub_size, sub_dirs, sub_files = analyze_directory(path)
            total_size += sub_size
            dir_count += sub_dirs
            file_count += sub_files

    return total_size, dir_count, file_count

#выбор директории для работы и пути к ней
main_path = os.path.abspath(os.path.join('..','..', '18_List_comprehensions'))
print(f"Анализируем директорию: {main_path}")

#запуск функции
total_size, dir_count, file_count = analyze_directory(main_path)

#выводим результаты
print("\nИтоговая статистика:")
print(f"Размер каталога (в Кб): {total_size} байт ({total_size / 1024:.2f} КБ)")
print(f"Количество подкаталогов: {dir_count}")
print(f"Количество файлов: {file_count}")