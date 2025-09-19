#Challenge
def factorial(num):
    #условие сотановки рекурсии
    if num == 1:
        return 1
    #умножаем вводимое значеине на функцию значение минус единица
    factorial_num = num * factorial(num - 1)
    return factorial_num
#выводим результат работы функции
N = int(input('введите номер: '))
result = factorial(N)
print(f"Факториал от числа {N}: {result}")