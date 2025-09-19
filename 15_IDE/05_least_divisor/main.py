# Наименьший делитель
import math
n = int(input('введите число: '))
def smallest_divisor(n):
    if n <= 1:
        return print('Не имеет делителей кроме 1')
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print('наименьший делитель равен: ',i)
                return i
        print('наименьший делитель равен: ', n)
        return n

perem = smallest_divisor(n)
