# IP - адрес 2
#меняе мразделители в адресе на точки
addres = input('Введите IP адресс: ').replace(',', '.').replace(';', '.').replace(' ', '.')
#переводим строку в список
addres = addres.split('.')
#создаем проверку на корректность цифр в адресе
def is_int(s):
    if not s.isdigit():
        return False
    num = int(s)
    return 0 <= num <= 255
#проверяем корректность IP-адреса
if len(addres) != 4:
    print('Ошибка: IP-адрес должен состоять из 4 чисел, разделенных точками')
else:
    valid = True
    for i in addres:
        if not is_int(i):
            print(f'Ошибка: "{i}" не является числом от 0 до 255')
            valid = False
            break

    if valid:
        #собираем список в строку
        ip_address = '.'.join(addres)

        print('IP-адрес корректен: ',ip_address)
