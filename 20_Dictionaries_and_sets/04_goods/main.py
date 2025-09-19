goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Товары

#создаём словарь для хранения результатов
results = dict()
#пребираем все товары из словаря goods
for i_item in goods:
    #получаем информацию о товаре из store
    item_data = store.get(goods[i_item],[])
    #print(item_data)
    #считаем общее количество и стоимость
    total_quantity = 0
    total_price = 0

    for idx in item_data:
        total_quantity += idx['quantity']
        total_price += idx['quantity'] * idx['price']

    #добавляем результаты в словарь
    results[i_item] = {
        'Количество': total_quantity,
        'Общая стоимость': total_price
    }
#print(results)
#выводим результаты циклом

for item_name in results:
    print(f'{item_name}',end='')
    print(f' - {results[item_name]['Количество']} шт,',end='')
    print(f' стоимость {results[item_name]['Общая стоимость']} руб')
