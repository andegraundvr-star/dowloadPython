#Контакты
phone_book = {}  #создаем пустой словарь

for _ in range(100):
    start_line = input('Введите имя, фамилию и телефон через пробел (или "стоп" для завершения): ').strip()

    #проверка на команду остановки
    if start_line.lower() == 'стоп':
        break
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
#выводим с помощью items
print(f"Текущий словарь контаков: ")
for phone_key, i_nomber in phone_book.items():
    print(f"        {' '.join(phone_key)} -- {i_nomber}")
