#пакеты
sum_pack = int(input('введите количество переданных пакетов: '))
getting_text = []
line_bit = []
count = 0
error_text = 0
for i_pak in range(1, sum_pack + 1):
    print('\nпакет номер ', i_pak)

    for i_nom in range(1, 5):
        print(i_nom, 'бит: ', end = ' ')
        bit = input()
        line_bit.append(bit)
        #print('line_bit',line_bit)
    if line_bit.count('-1') > 1:
        print('Много ошибок в пакете.')
        line_bit = []
        count += 1
        continue
    else:
        #print('Кол-во ошибок в сообщении: ',line_bit.count('-1'))
        error_text += line_bit.count('-1')
        getting_text.extend(line_bit)
        line_bit = []
    print('Полученное сообщение: ',getting_text)
    print('Кол-во ошибок в сообщении: ',error_text)
    print('Кол-во потерянных пакетов: ',count)