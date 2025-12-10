# Сообщение
import re

text = input('Введите сообщеине: ')
#с помощью метода re разбиваем строку на слова и заданные разделители
words_and_delimiters = re.split(r'([ ,;.!?:-])', text)
#print(words_and_delimiters)
reversed_text = []
#с помощью метода reversed меняем буквы в обратном порядке в каждом элементе списка
for i in words_and_delimiters:
    reversed_i = ''.join(reversed(i))
    reversed_text.append(reversed_i)
#собираем список обратно в строку
mem_text = ''.join(reversed_text)
print('Новое сообщение: ',mem_text)
