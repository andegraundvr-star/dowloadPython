#Словарь квадратов чисел
num = int(input('введите конечное число: '))
#создаем список чисел
number_list = [x for x in range(1,num + 1)]
#print(number_list)
#создаем словарь
disc = {x: x ** 2 for x in number_list}
print('Словарь квадратов:', disc)
