#Собачьи бега
list_of_dogs = int(input('введите количество собак: '))
dif_points = []

for idx_dog in range(list_of_dogs):
    print('количество очков у ', idx_dog + 1,'собаки равно ', end = '')
    point = int(input())
    dif_points.append(point)
print('ошибочный список призовых мест: ',dif_points)
maximum = dif_points[0]
minimum = dif_points[0]

for idx in dif_points:
    if maximum < idx:
        maximum = idx
    if minimum > idx:
        minimum = idx

print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)

new_list = []

for i in dif_points:
    if i == minimum:
        i = maximum
    elif i == maximum:
        i = minimum
    new_list.append(i)

print('верный список призовых мест: ',new_list)
