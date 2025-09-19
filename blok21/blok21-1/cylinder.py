# Цилиндр
import math
R = int(input('введите радиус основания цилиндра: '))
h = int(input('введите высоту цилиндра: '))
#создание функции с выводом двух значений
def parametrs(R,h):
    side = 2 * math.pi * R * h
    full = 2 * math.pi * R * (R + h)
    return side, full
#вычисление параметров
side, full = parametrs(R, h)
print(f'площадь боковой поверхности цилиндра равна {round(side,2)},\nполная площадь поверхности равна {round(full,2)}')