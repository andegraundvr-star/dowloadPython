# Уникальные элементы
while True:
    list_1 = list(input('введите первый список из трех чисел: '))
    if len(list_1) == 3:
        list_1 = list(list_1)
        break
    else:
        print('Ошибка! Нужно ввести ровно 3 цифры. Попробуйте ещё раз.')

while True:
    list_2 = list(input('введите второй список из 7-ми чисел: '))
    if len(list_2) == 7:
        list_2 = list(list_2)
        break
    else:
        print('Ошибка! Нужно ввести ровно 7 цифр. Попробуйте ещё раз.')
print('Первый список: ',list_1)
print('Второй список: ',list_2)
list_1.extend(list_2)
list_1 = list(set(list_1))
print('Новый первый список с уникальными элементами: ',list_1)
