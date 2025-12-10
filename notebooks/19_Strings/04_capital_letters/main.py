# Заглавные буквы
#преобразуем строку в список
enter_line = input('введите строку: ').split()
#меняем первую букву в каждом элементе списка на заглавную с помощью среза
new_line = []
for i in enter_line:
    word = str(i)
    #print(word)
    capitalized_word = word[0].upper() + word[1:]
    #собираем новый список из слов с заглавными буквами
    new_line.append(capitalized_word)
#переводим список в строку
true_frase = ' '.join(new_line)
print('Результат ',true_frase)






