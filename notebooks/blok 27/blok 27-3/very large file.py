# Очень большой файл
import os
#задаем путь к файлам
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', 'blok 27', 'blok 27-3')
path_file = os.path.join(path_dir, 'numbers.txt')

#функция проверяет, является ли этот знак числом
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
#генератор для чтения и обработки чисел из файла
def numbers_generator(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  #если строка не пустая
                    #разбиваем строку на части и обрабатываем каждую
                    parts = line.split()
                    for part in parts:
                        if is_number(part):
                            yield float(part)
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return
#чтение файла и подсчет суммы
try:
    total_sum = 0
    count = 0
    print(f"Содержимое файла {path_file}:")
    #используем генератор для чтения чисел
    gen = numbers_generator(path_file)

    #собираем все числа и считаем сумму
    numbers_list = []
    for number in gen:
        total_sum += number
        count += 1
        numbers_list.append(number)

    print(f"Все числа из файла: {numbers_list}")
    print(f"Количество чисел: {count}")
    print(f"Сумма всех чисел в файле равна: {total_sum}")

except Exception as e:
    print(f"Произошла ошибка: {e}")