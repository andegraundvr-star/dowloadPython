# Видеокарты
quantity = int(input('введите количество: '))
list_of_video = []
new_list = []
maksimum = 0
for _ in range(quantity):
    print('видеокарты в наличии: ', end = '')
    model = input()
    list_of_video.append(model)
    if int(model) > maksimum:
        maksimum = int(model)
print('старый список видеокарт: ',list_of_video)
for index_video in list_of_video:
    if int(index_video) < int(maksimum):
        new_list.append(index_video)
    else:
        continue
print('новый список видеокарт: ',new_list)




