#Создание кортежей
import random
#создаем два списка чисел с помошью метода random
start_list = [random.randint(0,5) for _ in range(10)]
two_list = [random.randint(-5,0) for _ in range(10)]
#переводим списки в кортежи
start_tuple = tuple(start_list)
two_tuple = tuple(two_list)
print(start_tuple)
print(two_tuple)
#объединяем кортежи с помощью метода __add__
new_tuple = start_tuple.__add__(two_tuple)
print(new_tuple)
#считаем нули в кортеже с помощью метода count
zero_count = new_tuple.count(0)
print(zero_count)