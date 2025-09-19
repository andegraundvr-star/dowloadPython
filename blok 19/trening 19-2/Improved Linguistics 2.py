#Улучшенная логистика
list_text = input('введите список слов через пробел: ').split( )
your_line = input('введите текст: ').split( ) #разбиваем текст на слова
count = 0
#print(list_text)
#print(your_line)
#создаем список для учета найденных слов (с повторами)
found_words = []
#ищем слова из вредложения в списке слов
for i in list_text:
    if i in your_line:
        found_words.append(i)
        #print(f'найдено слово {i} и помещено в специальный список {found_words}. Совпадений: {found_words.count(i)}')
        #count +=1
#используем цикл для подсчета повторов каждого слова
for word in set(found_words):  # используем set() для уникальных слов
    count = found_words.count(word)
    print(f"Слово '{word}' встречается {count} раз(а)")