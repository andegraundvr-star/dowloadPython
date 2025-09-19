#IP-адрес
ip_list = []
#создаем список из чисел
for _ in range(4):
    #в список добавляем условия для нужного ввода правильных чисел
    while True:
        number = input('введите число, часть IP адреса: ')
        if 0 <= int(number) <= 255:
            ip_list.append(number)
            break
        else:
            print('Каждое число находится в диапазоне от 0 до 255 (включительно)')
#сборка чисел из списка в строку через .format()
ip_address = '{0}.{1}.{2}.{3}'.format(ip_list[0], ip_list[1], ip_list[2], ip_list[3])
print(ip_address)
