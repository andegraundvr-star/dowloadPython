#Саботаж!
line = 'so~mec~od~e'
print('Строка: ',line)
print('Ответ: ',end='')
#присваиваем переменную к вновь изготовленному списку из ключей по нужному значению
tilde_indices = [str(idx) for idx, value in enumerate(line) if value == '~']
#переводим список ключей в строку с одновременным выводом
print(f"{' '.join(tilde_indices)}")