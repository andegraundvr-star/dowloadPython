#Повышение цен
sequence = []
#составляем список цен путем поочередного ввода
for i in range(5):
    price = float(input('цена на товар: '))
    sequence.append(price)
print(sequence)

year_1 = int(input('Повышение на первый год: '))
year_2 = int(input('Повышение на второй год: '))
#находим значения новых цен с учетом повышения за первый год
up_year_1 = [round(x + (x * year_1) / 100,2)  for x in sequence]
#print(up_year_1)
#находим значения новых цен с учетом повышения за второй год
up_year_2 = [round(x + (x * year_2) / 100,2) for x in sequence]
#print(up_year_2)
#находим сумму цен элементов списка за все года
summ_price = [sum(x) for x in zip(sequence, up_year_1, up_year_2)]
print(summ_price)
#находим сумму всех цен за каждый год
print('сумма цен за каждый год: ', round(sum(sequence),2), round(sum(up_year_1),2), round(sum(up_year_2),2))