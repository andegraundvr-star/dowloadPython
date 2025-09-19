# Дзен Пайтона 2
#открываем файл для записи всех данных один раз
with open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\02_zen_of_python\zen.txt', 'r', encoding='utf-8') as file_zen:
    count_simbol = 0
    count_word = 0
    count_phrase = 0
    all_text = ''

    #создаем функцию счета букв в предложении
    def sum_simbol_of_text(our_line):
        our_dict = dict()
        for i in our_line.lower():#привеодим сразу к нижнему регистру
            #количество букв суммируется при нахождении повторений
            if i in our_dict:
                our_dict[i] += 1
            #значеинию счетчика присваивается 1 при первом рассмотрении данной буквы
            else:
                our_dict[i] = 1
        return our_dict

    #т.к. в файле записана первая строка без переноса, читаем все строки, сохраняя оригинальные переносы
    lines = file_zen.readlines()

    for line in lines:
        #подсчет символов в строке (исключая добавленный позже \n)
        clean_line = line.rstrip('\n')
        count_simbol += len(clean_line)

        #подсчет слов
        words = clean_line.split()
        count_word += len(words)

        #собираем весь текст для анализа букв
        all_text += clean_line + ' '

    #для анализа символов приводим регистр букв к одному значению
    lower_lines = all_text.lower()
    #применяем функцию к переменной текста
    resultat = sum_simbol_of_text(lower_lines)
    # print(resultat)

    #с помощью цикла выстраиваем ключ-значение вериткально и добавляем метод сортировки
    print(f"Полная статистика по символам:")
    for i in sorted(resultat.keys()):
        print(i, ':', resultat[i])
    #находим ключ максимального значения в словаре
    key_min_res = min(resultat, key=resultat.get)
    #выводим ключ макисмального значения и само значеине на экран
    print(f'\nМинимальный результат показал символ: "{key_min_res}" со значением счетчика: {min(resultat.values())}')

    #проверяем и исправляем переносы строк, а также делаем подсчет фраз
    for line in lines:
        if line.strip():
            #print(line, end='')
            count_phrase += 1
print(f"Всего символов (без переносов): {count_simbol}")
print(f"Всего слов: {count_word}")
print(f"Всего фраз: {count_phrase}")





