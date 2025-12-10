#Функция сортировки

import random

numbers = []
#создаем случайный номер с типом float и округляем до двух знаков
secret_nomber = round(random.uniform(1.0, 20.0), 2)
#создаем список случайной длинны
for _ in range(random.randint(3, 7)):
    #наполняем список случайными числами
    numbers.append(random.randint(1, 20))
    #without_secret = numbers[:]
#прописываем рандомное добавление числа с десятичными долями
if random.choice([True, False]):
    numbers.append(secret_nomber)
#преобразуем в кортеж
numbers = tuple(numbers)
print("Случайный перемешанный кортеж:", numbers)
#сама функция
def sort_random(tuple):
    if secret_nomber not in numbers:
        return sorted((numbers))
    else:
        return numbers
#вывод результата вызова функции
print(sort_random(numbers))