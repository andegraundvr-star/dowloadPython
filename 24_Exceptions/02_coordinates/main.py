# Координаты
import random
import os


def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    try:
        return x / y
    except ZeroDivisionError:
        return float('inf')  #или другое значение по умолчанию

def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    try:
        return y / x
    except ZeroDivisionError:
        return float('inf')  #или другое значение по умолчанию
#задаем путь к файлам
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', '24_Exceptions', '02_coordinates')
path_file = os.path.join(path_dir, 'coordinates.txt')
output_path = os.path.join(base_dir, 'python-ds', '24_Exceptions', '02_coordinates')
output_file = os.path.join(output_path, 'result.txt')

#создаем функцию для редактирования строк в файле
def redact_text(file_line):
    try:
        #преобразуем строку в два числа (формат "x y")
        nums = list(map(int, file_line.strip().split()))
        if len(nums) != 2:
            raise ValueError("Ожидается ровно два числа в строке")

        #вычисляем результаты функций
        result_f = f(nums[0], nums[1])
        result_f2 = f2(nums[0], nums[1])

        return result_f, result_f2
    except ValueError as e:
        print(f"Ошибка в строке '{file_line.strip()}': {e}")
        return None

#проверяем существование файла перед открытием
if not os.path.exists(path_file):
    raise FileNotFoundError(f"Файл не найден: {path_file}")

#чтение файла
try:
    with open (path_file, 'r', encoding = 'utf-8') as file_with_nombers:
        print(f"Содержимое файла {path_file}:")
        #собираем все результаты в список для сортировки
        results = []
        for line in file_with_nombers:
            result = redact_text(line)
            if result is not None:
                rand_num = random.randint(0, 100)
                #сохраняем как кортеж (случайное число, результаты)
                results.append((rand_num, result[0], result[1]))

        #сортируем по случайному числу (первый элемент кортежа)
        results.sort()
        #сохраняем содержимое в файл
        with open(output_file, 'w', encoding='utf-8') as file_to:
            for item in results:
                #форматируем строку: случайное число, результат f, результат f2
                output_line = f"{item[0]} {item[1]} {item[2]}\n"
                file_to.write(output_line)
                print(f'Добавлено: {output_line.strip()}')
except Exception as e:
    print(f"Произошла ошибка: {e}")


