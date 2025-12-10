# Регистрация

import os

#задаем путь к файлам
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', '24_Exceptions', '04_registration')
path_file = os.path.join(path_dir, 'registrations.txt')
output_path = os.path.join(base_dir, 'python-ds', '24_Exceptions', '04_registration')
output_file_good = os.path.join(output_path, 'registrations_good.log')
output_file_bad = os.path.join(output_path, 'registrations_bad.log')

#функция заданных исключений
def raise_exception(number):
    exceptions = {
        1: 'IndexError: неверный формат данных, должно быть три поля',
        2: 'NameError: в поле имя должны содержаться только буквы',
        3: 'SyntaxError: поле email должно содержать @ и .',
        4: 'ValueError: поле возраст должно быть числом от 10 до 99'
    }
    if number not in exceptions:
        raise ValueError("Номер исключения должен быть от 1 до 4")
    raise Exception(exceptions[number])

#функция проверки на условия
def check_condition(line):
    parts = line.strip().split()

    #проверка 1
    if len(parts) != 3:
        raise_exception(1)

    name, email, age = parts

    #проверка 2
    if not name.isalpha():
        raise_exception(2)

    #проверка 3
    if '@' not in email or '.' not in email:
        raise_exception(3)

    #проверка 4
    try:
        age_num = int(age)
        if age_num < 10 or age_num > 99:
            raise_exception(4)
    except ValueError:
        raise_exception(4)

    return True

#чтение файла
try:
    results_good = []
    results_bad = []

    with open(path_file, 'r', encoding='utf-8') as file_with_info:
        print(f"Содержимое файла {path_file}:")

        for line in file_with_info:
            line = line.strip()
            if not line:  #пропускаем пустые строки
                continue
            #создаем списки с верными и не верными строками
            try:
                if check_condition(line):
                    results_good.append(line)
            except Exception as e:
                #добавляем в список строку и ошибку
                results_bad.append(f"{line}    # {str(e)}")

    #сохраняем содержимое в файлы
    with open(output_file_good, 'w', encoding='utf-8') as file_to_good:
        for item in results_good:
            file_to_good.write(item + '\n')
            print(f'Добавлено в good: {item}')

    with open(output_file_bad, 'w', encoding='utf-8') as file_to_bad:
        for item in results_bad:
            file_to_bad.write(item + '\n')
            print(f'Добавлено в bad: {item}')

except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")