#Улучшенная лингвистика
words_list = []
counts = [0,0,0]
for i in range(3):
    print('введите', i + 1, 'слово: ', end='')
    word = input()
    words_list.append(word)

in_text = input('введите слово из текста: ')

while in_text != 'end':
   for index in range(3):
       if words_list[index] == in_text:
           counts[index] += 1
   in_text = input('введите слово: ')

print('\nподсчет слов: ')
for i in range(3):
    print('слово', words_list[i],'встречается в тексте', counts[i],'раз')