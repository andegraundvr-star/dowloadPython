#Логирование

import os
from datetime import datetime

#задаем путь к файлу
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', 'blok 24', '24-3')
path_file = os.path.join(path_dir, 'word.txt')

#проверяем существование файла перед открытием
if not os.path.exists(path_file):
    raise FileNotFoundError(f"Файл не найден: {path_file}")
#файл для ошибок
error = os.path.join(path_dir, 'error.log')
#чтение файла

#открываем файл для записи ошибок
with open(error, 'a', encoding='utf-8') as error_log:
    error_log.write(f"\n\n=== Проверка палиндромов {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
    try:
        with open(path_file, 'r', encoding='utf-8') as start_file:
            summ_p = 0
            print(f"Содержимое файла {path_file}:")
            for  line in start_file:
                #добавляем блок try-except для обработки ошибок в каждой строке
                try:
                    if line.strip().lower().replace(' ', ''):  #пропускаем пустые строки. приводим к нижнему регистру и удаляем пробелы
                        if line == line[::-1]:
                            summ_p += 1
                        else:
                            #проверяем, можно ли сделать палиндром перестановкой символов
                            item_count = dict()
                            for item in line:
                                item_count[item] = item_count.get(item, 0) + 1

                            odd_counts = 0 #счётчик слов с нечётным количеством
                            #перебираем все количества повторений слов
                            for count in item_count.values():
                                #проверяем, нечётное ли это число
                                if count % 2 != 0:
                                    #если число нечетное - увеличиваем счётчик
                                    odd_counts += 1
                            #выводим условие на одно нечетное число повторений
                            if odd_counts <= 1:
                                summ_p += 1
                            else:
                                #логируем слово, не являющееся палиндромом
                                error_msg = f"Строка {line}: '{line.strip()}' не является палиндромом\n"
                                error_log.write(error_msg)
                                print(error_msg.strip())
                except Exception as e:
                    error_log.write(f"Ошибка обработки строки: {line} - {str(e)}\n")

            print(f"Всего палиндромов в файле: {summ_p}")
            error_log.write(f"Итого: {summ_p} палиндром(ов) найдено\n")
    #добавялем стандартный пул обработки ошибок
    except UnicodeDecodeError:
        print("Ошибка: файл имеет неверную кодировку")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
