#Гистограмма частоты
#создаем функцию счета букв в предложении
def sum_simbol_of_text(our_line):
    our_dict = dict()
    for i in our_line:
        #количество букв суммируется при нахождении повторений
        if i in our_dict:
            our_dict[i] += 1
        #значеинию счетчика присваивается 1 при первом рассмотрении данной буквы
        else:
            our_dict[i] = 1
    return our_dict
#вводим сам текст и применяем функцию
text = input('введите текст: ').lower()
resultat = sum_simbol_of_text(text)
#print(resultat)
#с помощью цикла выстраиваем ключ-значение вериткально и добавляем метод сортировки
for i in sorted(resultat.keys()):
    print(i,':',resultat[i])
#находим ключ максимального значения в словаре
key_max_res = max(resultat, key=resultat.get)
#выводим ключь макисмального значения и само значеине на экран
print(f'\nмаксимальный результат буква показала: {key_max_res} со значением счетчика: {max(resultat.values())}')
