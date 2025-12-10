#Таблица степеней
numbers = [3,7,5]

while True:

    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    res = []
    two = []
    three = []

    for x in numbers:
        res.append(x ** 2)
        two.append(x ** 3)
        three.append(x ** 4)
    print("кадое число списка во 2 степени : " + str(res))
    print("кадое число списка в 3 степени : " + str(two))
    print("кадое число списка в 4 степени : " + str(three))

print()
