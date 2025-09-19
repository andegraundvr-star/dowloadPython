# Словарь синонимов
N = int(input('введите количество пар слов: '))
start_dict = dict()
for _ in range(N):
    while True:
        #добавление синонимов в списки
        main_sub = input('Введите пару синонимов через пробел: ').lower().split()
        #проверка списка на количество знвчений
        if len(main_sub) == 2:
            word1, word2 = main_sub
            #добавление ключей и значеинй в начальный словарь
            start_dict[word1] = word2
            start_dict[word2] = word1
            break
        else:
            print('Ошибка: нужно ввести ровно два слова через пробел')

print('\nСловарь синонимов создан:')
print(start_dict)

#реалицация цикла для поиска пар слов

for _ in range(3):
    duble = input('\nВведите слово для посика синонима: ').lower()
    if duble in start_dict:
        print(f'Синоним слова "{duble}" - "{start_dict[duble]}"')
    else:
        print(f'Слова "{duble}" нет в словаре.')