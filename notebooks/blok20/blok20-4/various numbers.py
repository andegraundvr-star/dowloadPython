#Различные цифры
text = input('введите строку: ')
nomber_count = set()
#в цикле собираем множество по двум условиям
for i in text:
    if i not in nomber_count and '0'<=i<='9':
        #print(i)
        nomber_count.add(i)
#преобразуем множество в отсортированный список и выводим значения через пробел
result = ' '.join(sorted(nomber_count))
print('Найденные цифры:', result)