#Неправильный код
import random

def change(nums):

    index = int(random.randint(0, 5))

    value = int(random.randint(100, 1000))
    #делаем копию кортежа списком
    changet_nums = list(nums[:])
    print(changet_nums)
    #заменяем одно значение в списке
    if index in nums:
        changet_nums[index] = value
    #перевдим список в новый кортеж
    new_nums = tuple(changet_nums)
    print(new_nums, value)
    return new_nums, value

rand_val = 0

my_nums = (1, 2, 3, 4, 5)

#первый вызов
my_nums, value = change(my_nums)
print(f'После второго изменения: {my_nums} Значение: {value}')
rand_val += value

#второй вызов
my_nums, value = change(my_nums)
print(f'После второго изменения: {my_nums} Значение: {value}')
rand_val += value

print("Сумма всех случайных значений:", rand_val)
#new_nums, rand_val = change(my_nums)

#print(new_nums, rand_val)

#new_nums = change(new_nums)

#rand_val += change(new_nums)

#print(new_nums, rand_val)