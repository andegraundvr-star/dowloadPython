#Детали
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
count = 0
price = 0
request = input('что ищете? ')
for item in shop:

        if item[0] == request:
                price += item[1]
                count += 1
if count < 1:
        print('такой детали нет в списке')
else:
        #print(request)
        print('количество: ', count)
        print('общая стоимость: ',price)
