# Монетка 2
import math
x = float(input('введите координату х: '))
y = float(input('введите координату y: '))
radius = float(input('введите радиус сканирования: '))
def is_coin_in_circle():

    print('дистанция до цели определяется по формуле: х = sqrt(x ** 2 + y ** 2)')

    distance = math.sqrt(x ** 2 + y ** 2)  # Расстояние от точки до центра (0, 0)
    if distance <= radius:
        return print('точка (',x,',',y,') принадлежит кругу с радиусом ', radius,', монетка найдена')
    else:
        return print('точка (',x,',',y,') не принадлежит кругу с радиусом ', radius,', монетка где-то рядом')
result = is_coin_in_circle()