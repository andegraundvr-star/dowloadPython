#Текстовый редактор
items = input('введите строку: ')
str_items = []
count_chenge = 0

for i in items:
    if i == ':':
        i = ';'
        count_chenge += 1
    str_items.append(i)

for i in str_items:
    print(i, end = '')
print('\nколичество замен: ',count_chenge)


