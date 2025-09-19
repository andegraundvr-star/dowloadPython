#Контакты 3
phone_book = {}  #создаем пустой словарь
#задаем переменную выбора действия
while True:
    change = input('Если хотите добавить имя, нажмите "1", найти контакт, нажмите "2", или "0" для завершения: ').strip()
    if change == '0':
        break
    elif change == '1':
        while True:
            start_line = input('Введите имя, фамилию и телефон через пробел (или "стоп" для завершения): ').strip()
            #print(start_line)
            #проверка на команду остановки
            if start_line.lower() == 'стоп':
                break
            #проверка на длинну ввода
            if len(start_line.split()) < 3:
                print('Ошибка: нужно ввести имя, фамилию и телефон через пробел')
                continue
            start_list = start_line.split(' ')
            #print(start_list[:2])
            #создание кортежа из имени и фамилии из среза списка и функции map
            first_name, second_name = map(str, start_list[:2])
            phone_key = (first_name, second_name)

            #проверка на существующее имя
            if phone_key in phone_book:
                print(f'Ошибка: имя "{' '.join(phone_key)}" уже есть в телефонной книге')
                continue
            #добавление ключей и значений в словарь
            phone_book[phone_key] = start_list[2]
            print(f"Добавлено")
    elif change == '2':
            #print(phone_book)
            target = input('Введите фамилию: ').lower()  # переводим в нижний регистр
            # удаляем окончание в фамилии женского рода
            if target.endswith(('а')):
                target = target[:-1]

            for i_key, i_value in phone_book.items():
                # создаем переменную из двух дначений кортежа ключа словаря
                name_key = [x for x in i_key]
                # проверка на соответсвие фамилии из словаря с введенной фамилией
                if name_key[0].endswith(('а')):
                    name_key[0] = name_key[0][:-1].lower()  # переводим в нижний регистр
                if target == name_key[0]:
                    #выводим ранее созданную переменную и значение словаря
                    print(f"\nВ телефонной книге найден контакт: ")
                    #for name_key, phone_value in phone_book.items():
                    print(f"{''.join(name_key[0])} {''.join(name_key[1])} -- {i_value}")
                    break
#выводим с помощью items
print(f"Текущий словарь контаков: ")
for phone_key, i_nomber in phone_book.items():
    print(f"        {' '.join(phone_key)} -- {i_nomber}")


