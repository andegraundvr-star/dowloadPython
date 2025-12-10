#Универсальная программа 2

print("Введите итерируемый объект: ", end='')
user_input = input().strip()
#функция для проверки индексов на простые числа
import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
#создаем основную функцию:
def base(line):
    #если ввод пустой, считаем его пустой строкой
    if not user_input:
        start_object = ""
    else:
        #проверяем, является ли ввод строкой в кавычках
        if (user_input[0] == user_input[-1] and user_input[0] in ('"', "'")):
            start_object = user_input[1:-1]  #убираем кавычки
        #проверяем, похож ли ввод на список или кортеж
        elif user_input.startswith(('(', '[')) and user_input.endswith((')', ']')):
            #обработка списка/кортежа (без вложенных структур)
            elements = user_input[1:-1].split(',')
            if user_input.startswith('['):
                start_object = [elem.strip() for elem in elements]
            else:
                start_object = tuple(elem.strip() for elem in elements)
        else:
            start_object = user_input  #иначе оставляем как строку

    #если объект не итерируемый, преобразуем в строку
    if not isinstance(start_object, (list, tuple, str)):
        start_object = str(start_object)

    result = [value for index, value in enumerate(start_object) if is_prime(index) == True]
    return result

print(f"\nРезультат: {base(user_input)}")