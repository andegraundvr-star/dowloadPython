#отряды
import random
#составляем списки с помощью метода рандом
group_1 = [random.randint(50, 80) for i in range(10)]
group_2 = [random.randint(30, 60)for i in range(10)]
#составляем третий список с условием
group_3 = [('погиб' if group_1[id] + group_2[id] > 100 else 'выжил') for id in range(10)]

print('урон первого отряда', group_1)
print('урон второго отряда', group_2)
print('состояние третьего отряда', group_3)