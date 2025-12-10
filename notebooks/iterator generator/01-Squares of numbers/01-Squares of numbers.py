#Квадраты чисел
"""Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
"""
#функция ввода конечного числа
def user_enters():
    while True:
        try:
            return int(input("Введите число N: "))
        except ValueError:
            print("Ошибка: введите целое число!")
#1. Класс-итератор
class Niter:
    #number_N = 0
    def __init__(self, n):
        self.n = n #задаем на входе конечное число в ряду
        self.current = 0  #текущее значение
        self.index = 0    #текущий индекс
    def __iter__(self):
        self.index = 0 #сбрасываем индекс для новой итерации
        self.current = 0
        return self
    def __next__(self):
        #задаем условие для стопа итерации
        if self.index > self.n:
            raise StopIteration
        result = self.index ** 2
        self.index += 1
        return result

#2. Функция-генератор
def squares_generator(n):
    for i in range(n + 1):
        yield i ** 2

#3. Генераторное выражение
def squares_expression(n):
    return (i ** 2 for i in range(n + 1))



#основная программа
n = user_enters()

print("1. Класс-итератор:", list(Niter(n)))
print("2. Функция-генератор:", list(squares_generator(n)))
print("3. Генераторное выражение:", list(squares_expression(n)))