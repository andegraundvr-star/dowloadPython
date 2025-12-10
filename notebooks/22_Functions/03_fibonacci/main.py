# Ряд Фибоначчи
N = int(input('Введите позицию в ряде Фибоначи: '))
def fibonacci(num):
    #создаем условия прекращения рекурсии
    if num <= 1:
        return []
    elif num == 2:
        return [1, 1]
    # создаем список и добавляем новые значения с помощью функции
    else:
        fib_list = fibonacci(num - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
#выводим результат с помощью среза последнего значения списка
result = fibonacci(N)
print(result)
print('На этой позиции стоит число: ',result[N-1:])
