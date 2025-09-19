# Сжатие списка
import random

N = int(input('введите количество целых чисел в строке: '))
#с помощью метода рандом создаем список заданной длинны
sequence = [random.randint(0,1) for i in range(N)]
print('изначальный список: ',sequence)
#сортировка циклами и сложение списков
sequence = [x for x in sequence if x > 0] + [x for x in sequence if x == 0]
print('отсортированный список с нулевыми значениями в конце списка: ',sequence)
#сортировка циклами без дополнительного сложения списков
sequence = [x for x in sequence if x > 0]
print('отсортированный список без нулевых значений в конце списка: ',sequence)