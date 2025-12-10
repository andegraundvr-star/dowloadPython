#Имена
import os
#задаем путь к файлу
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', 'blok 24', '24-3')
path_file = os.path.join(path_dir, 'people.txt')

#проверяем существование файла перед открытием
if not os.path.exists(path_file):
    raise FileNotFoundError(f"Файл не найден: {path_file}")

#чтение файла
try:
    with open(path_file, 'r', encoding='utf-8') as start_file:
        summ_simbol = 0
        print(f"Содержимое файла {path_file}:")
        for  line in start_file:
            #добавляем блок try-except для обработки ошибок в каждой строке
            try:
                if line.strip():  #пропускаем пустые строки
                    chars = len(line) - 1
                    if chars < 3:
                        raise BaseException(f"Строка {line} содержит меньше 3 символов: '{line.strip()}'")
                    else:
                        summ_simbol += chars
            except BaseException as be:
                print(f"Ошибка: {be}")
                break  #прерываем обработку файла при обнаружении ошибки
        #выводим результат вычислений (можно не выводить)
        print(f"всего символов: {summ_simbol}")
#добавялем стандартный пул обработки ошибок
except UnicodeDecodeError:
    print("Ошибка: файл имеет неверную кодировку")
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")