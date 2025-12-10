#Пунктуация помощью словаря
text = input('введите строку: ')
punct_count = {}
punct_type = {'.',',',';',':','!','?'}
#подсчитываем количество каждого знака препинания и добавляем в множество punct_count
for i in text:
    if i in punct_type:
        punct_count[i] = punct_count.get(i, 0) + 1
print('Количество знаков препинания: ', end='')
#с помощью метода суммы в словарях выводим количество в множистве punct_count
print(f'{sum(punct_count.values())}')
