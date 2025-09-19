# текстовый калькулятор 2

import os

#задаем путь к файлу
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', '24_Exceptions', '07_text_calc_2')
path_file = os.path.join(path_dir, 'calc2.txt')
#функция исправления ошибки
def correction():
    while True:
        operator = input('Введите правильный оператор (+, -, *, /, //): ')
        if operator in ('+', '-', '*', '/', '//'):
            return operator
        print("Некорректный оператор. Попробуйте снова.")
#функция "вычислить"
def calculate(operand1, operator, operand2):
    try:
        operand1 = float(operand1)
        operand2 = float(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            return operand1 / operand2
        elif operator == '//':
            if operand2 == 0:
                raise ZeroDivisionError("Целочисленное деление на ноль невозможно")
            return operand1 // operand2
    except ValueError:
        raise ValueError("Ошибка: операнды должны быть числами")
    except Exception as e:
        raise Exception(f"Ошибка вычисления: {e}")
#обработка одной строки из файла
def process_line(line, line_num):
    #пропускаем пустые строки
    line = line.strip()
    if not line:
        return None
    #проверка на корректность строки - 3 элемента
    try:
        parts = line.split()
        if len(parts) != 3:
            raise ValueError("Ошибка: строка должна содержать ровно 3 элемента")

        operand1, operator, operand2 = parts

        #проверка оператора
        if operator not in ('+', '-', '*', '/', '//'):
            print(f"\nОшибка в строке {line_num}: некорректный оператор '{operator}'")
            answer = input("Хотите исправить оператор? (да/нет): ").lower()
            if answer == 'да':
                operator = correction()
                #пересчитываем с новым оператором
                result = calculate(operand1, operator, operand2)
                print(f'Результат вычисления строки {line_num}) "{operand1} {operator} {operand2}": {result}')
                return result
            raise ValueError(f"Некорректный оператор: '{operator}'")

        result = calculate(operand1, operator, operand2)
        print(f'Результат вычисления строки {line_num}) "{line}": {result}')
        return result

    except Exception as e:
        raise e
#чтение файла
try:
    with open(path_file, 'r', encoding='utf-8') as file_matem:
        print(f"Содержимое файла {path_file}:")

        for line_num, line in enumerate(file_matem, 1):
            try:
                result = process_line(line, line_num)

            except ValueError as ve:
                print(f"Ошибка в строке {line_num}) '{line}': {ve}")
            except ZeroDivisionError as zde:
                print(f"Ошибка в строке {line_num} '{line}': {zde}")
            except Exception as e:
                print(f"Неизвестная ошибка в строке {line_num} '{line}': {e}")

except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
finally:
    print("\nОбработка файла завершена")

