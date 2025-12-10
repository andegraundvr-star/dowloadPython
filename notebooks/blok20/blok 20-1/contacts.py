#Контакты
phone_book = {}  #создаем пустой словарь

for _ in range(100):
    start_line = input('Введите имя и телефон через пробел (или "стоп" для завершения): ').strip()

    # Проверка на команду остановки
    if start_line.lower() == 'стоп':
        break
    start_list = start_line.split()

    # Проверка на существующее имя
    if start_list[0] in phone_book:
        print(f'Ошибка: имя "{start_list[0]}" уже есть в телефонной книге')
        continue
    # Добавление ключей и значений в словарь
    phone_book[start_list[0]] = start_list[1]
    print(f'Добавлено: {start_list[0]} - {start_list[1]}')

# Выводим итоговую телефонную книгу циклом
print('\nТелефонная книга:')
for name, phone in phone_book.items():
    print(f'{name}: {phone}')