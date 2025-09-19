# Родословная
N = int(input('Введите количество человек: '))
levels = dict()

print('Вводите пары в формате: "ребёнок родитель"')
#сначала делаем словарь уровней
for i in range(N - 1):
    while True:  #цикл для повторного ввода при ошибке
            print(f'{i + 1} пара: ',end = '')
            parts = input().split()
            if len(parts) != 2:
                print('Ошибка: нужно ввести ровно два имени через пробел. Попробуйте еще раз.')
                continue
            child, parent = parts
            if parent not in levels:
                levels[parent] = 0
            levels[child] = levels[parent] + 1
            break

#группируем людей по уровням
level_groups = dict()
for person, level in levels.items():
    if level not in level_groups:
        level_groups[level] = []
    level_groups[level].append(person)

#выводим результат циклом
print(f'\nВысота” каждого члена семьи:')
for person, level in levels.items():
    print(f'{person}:{level}')