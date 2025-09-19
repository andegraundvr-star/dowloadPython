#Список квадратов чётных чисел
A = int(input('начало диапазона: '))
B = int(input('конец диапазона: '))
#выводим список чисел из указаного диапазона с помощью "list comprehensions"
squares_of_numbers_1 = [x for x in range(A,B + 1) if x % 2 == 0]
print('список четных чисел из диапазона: ',squares_of_numbers_1)
#находим квадраты чисел с помощью "list comprehensions"
squares_of_numbers = [x ** 2 for x in range(A,B + 1) if x % 2 == 0]
print('список квадратов четных чисел из диапазона: ',squares_of_numbers)
