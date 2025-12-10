# Пицца
order_count = int(input('введите количество заказов: '))
order_dict = dict()
print(f'Введите имя,  название заказа и количество через пробел: ')
for i in range(order_count):
    start_line = input(f'{i + 1} заказ: ').split()
    name, pizza, quantity = start_line
    quantity = int(quantity)
    #добавление ключей и значений в словарь
    if name not in order_dict:
        order_dict[name] = dict()
    #суммируем количество одинаковых хаказов у одного человека
    if pizza in order_dict[name]:
        order_dict[name][pizza] += quantity
    else:
        order_dict[name][pizza] = quantity

    #print(f'{i + 1} заказ: {name} - {pizza} {quantity}')

#выводим отсортированный список заказов
print('\nИтоговые заказы:')
for name in sorted(order_dict):
    print(f'{name}:')
    for pizza, quantity in sorted(order_dict[name].items()):
        print(f'         {pizza}: {quantity}')