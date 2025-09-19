# Текстовый калькулятор
import os

#задаем путь к файлу
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', '24_Exceptions', '05_text_calc')
path_file = os.path.join(path_dir, 'calc.txt')

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
        else:
            raise ValueError(f"Неизвестный оператор: {operator}")
    except ValueError as ve:
        raise ValueError(f"Ошибка преобразования числа: {ve}")
    except Exception as e:
        raise Exception(f"Ошибка вычисления: {e}")
#чтение файла
try:
    with open(path_file, 'r', encoding='utf-8') as file_matem:
        print(f"Содержимое файла {path_file}:")

        for line_num, line in enumerate(file_matem, 1):
            line = line.strip()
            if not line:  #пропускаем пустые строки
                continue

            try:
                parts = line.split()
                if len(parts) != 3:
                    raise ValueError("Строка должна содержать ровно 3 элемента: два операнда и оператор")

                operand1, operator, operand2 = parts

                result = calculate(operand1, operator, operand2)
                print(f'Результат вычисления строки {line_num} "{line}": {result}')

            except ValueError as ve:
                print(f"Ошибка в строке {line_num} '{line}': {ve}")
            except ZeroDivisionError as zde:
                print(f"Ошибка в строке {line_num} '{line}': {zde}")
            except Exception as e:
                print(f"Неизвестная ошибка в строке {line_num} '{line}': {e}")

except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")


