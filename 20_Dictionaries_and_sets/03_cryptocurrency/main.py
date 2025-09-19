data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "totalOut": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


#Криптовалюта
print(f'\nСписок ключей и значений словаря:')
for i in data:
    print(f'ключ: {i}, значение {data[i]}')

#добавляем ключ и значение в структуре ETH
if 'total_diff' not in data['ETH']:
    data['ETH']['total_diff'] = 100

#переименовываем 'fdf' в 'doge' во вложенной структуре
for i_token in data['tokens']:
    if 'fst_token_info' in i_token and i_token['fst_token_info']['name'] == 'fdf':
        i_token['fst_token_info']['name'] = 'doge'

#добавляем значение total_out в структуру data['ETH']
if 'total_out' in data['ETH'] != 0:
    data['ETH']['total_out'] = 0

#удаляем total_out из структуры ['tokens']
for i_token in data['tokens']:
    if 'total_out' in i_token:
        del i_token['total_out']

# Ищем токен с sec_token_info во всем списке tokens
for i_token in data['tokens']:
    if 'sec_token_info' in i_token:
        #проверяем наличие ключа 'price' в sec_token_info
        if 'price' in i_token['sec_token_info']:
            #переименовываем 'price' в 'total_price'
            i_token['sec_token_info']['total_price'] = i_token['sec_token_info'].pop('price')

print(f'\nИзмененный список ключей и значений словаря:')
for i in data:
    print(f'ключ: {i}, значение {data[i]}')


