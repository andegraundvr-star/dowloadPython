# Свой zip
#записываем услвие
start_line = 'abcd'
srat_tuple = (10, 20, 30, 40)
print(f"Строка: {start_line} \nКортеж из чисел: {srat_tuple}")

#преобразуем строку и кортеж в списки
start_list = list('abcd')
tuple_list = list(srat_tuple)

#создаём собственный "zip" - объединяем элементы попарно,определив минимальную длинну списков
custom_zip = ((start_list[i], tuple_list[i]) for i in range(min(len(start_list), len(tuple_list))))

#выводим генератор и кортежи из списка
print(f"Результат: ")
print(custom_zip)
for pair in custom_zip:
    print(f"{pair}")