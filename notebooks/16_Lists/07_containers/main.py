# Контейнеры
row = []
new_row = []
total_number = int(input('введите число контейнеров: '))
for i in range(total_number):
    print('введите вес контейнера: ', end = '')
    weight = input()
    if int(weight).is_integer():
        if int(weight) > 200:
            print('вес не может превышать 200 кг')
            continue
    else:
        print('введите целое число')
        continue
    row.append(weight)
#print(row)
new_container = int(input('введите вес нового контейнера: '))

for i in row:
    while int(i) <= new_container:
        new_row.append(i)
        break
new_row.append(new_container)
for i in row:
    while int(i) > new_container:
        new_row.append(i)
        break
count = 0
#print(new_row)
for i in new_row:
    count += 1
    if i == new_container:
        break
print('Номер, куда встанет новый контейнер: ',count)


