#Кастомные исключения
import os

#создаем собственный класс исключения
#кастомное исключение для ошибок деления
class DivisionError(Exception):
    pass
#еще один кастомный класс ошибки
#Ошибка пустой строки
class EmptyLineError(Exception):
    pass
#еще один кастомный класс ошибки
#Ошибка формата чисел
class NumberFormatError(Exception):
    pass

#задаем путь к файлам
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', 'blok 26', 'blok 26-2')
path_file = os.path.join(path_dir, 'lucky.txt')


#функция заданных исключений
def check_condition(line):
    exceptions = 'ValueError: нельзя делить большее на меньшее'
    #проверка
    try:
        numbers = list(map(int, line.split()))  #преобразуем строку в числа сразу
        if numbers[0] < numbers[1]:
            result = round(numbers[0] / numbers[1], 2)
            return result
        else:
            #используем наше кастомное исключение
            raise DivisionError("нельзя делить большее на меньшее")
    except ValueError:
        #также используем кастомное исключение для ошибок преобразования
        raise DivisionError("неверный формат чисел")

#чтение файла
try:
    results_good = []
    results_bad = []
    with open(path_file, 'r', encoding='utf-8') as file_with_info:
        print(f"Содержимое файла {path_file}:")
        for line in file_with_info:
            if not line.strip():
                raise EmptyLineError("пустая строка")
            #создаем список со строками, удовлетворяющим условию
            try:
                result = check_condition(line)  #получаем результат
                if result is not None:  #если результат есть
                    results_good.append(result)  #добавляем в хорошие результаты
                    print(f"результат деления меньшего числа на большее: {result}")
            except DivisionError as e:
                #добавляем в список строку и ошибку
                results_bad.append(f"{line}    # DivisionError: {str(e)}")
            #записываем в список результаты других ошибок
            except NumberFormatError as e:
                results_bad.append((line, f"NumberFormatError: {e}"))
            except EmptyLineError as e:
                results_bad.append((line, f"EmptyLineError: {e}"))
            except Exception as e:
                #добавляем другие ошибки
                results_bad.append(f"{line}    # {type(e).__name__}: {str(e)}")
except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")