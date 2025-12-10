# Генерация списка
N = int(input('введите число N: '))
new_list = []
for i in range(N+1):
    if i % 2 != 0:
        new_list.append(i)
print(new_list)
