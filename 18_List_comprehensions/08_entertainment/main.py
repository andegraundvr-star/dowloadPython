# Развлечение
import random

N = int(input('Количество палок: '))
K = int(input('Количество бросков: '))
#создаем переменную: 1 - палка стоит, 0 - сбита
sticks = [1] * N

for throw in range(1, K + 1):
    print('Бросок', throw)

    #генерируем удар: случайные палки сбиваются
    hit = [random.randint(0, 1) for _ in range(N)]
    #print("Результат удара:", hit)

    #обновляем состояние палок
    for i in range(N):
        if hit[i] == 0 and sticks[i] == 1:  # Если палка стояла и сбита
            sticks[i] = 0

    #находим диапазоны сбитых палок
    ranges = []
    start = None
    for i in range(N + 1):
        if i < N and sticks[i] == 0:
            if start is None:
                start = i
        else:
            if start is not None:
                ranges.append(str(start + 1) + '-' + str(i))
                start = None

    print('Сбиты палки с номерами:', ', '.join(ranges) if ranges else 'нет')
    print('Текущее состояние палок:', sticks)
    #считаем количество оставшихся палок
    remaining = sum(sticks)
    #print('Осталось палок: ',remaining)

    if remaining == 0:
        print('Все палки сбиты!')
        break

if sum(sticks) > 0:
    print('Не все палки сбиты!')