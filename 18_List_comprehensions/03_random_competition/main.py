# Случайные соревнования
import random
#создаем два списка команд с помощью метода random с последующем округлением до двух знаков
command_1 = [round(random.uniform(5,10),2) for i in range(20)]
command_2 = [round(random.uniform(5,10),2) for j in range(20)]
#создаем номый список с условиями сравнения каждого элемента двух списков и выводом наибольшего значения
champions = [command_1[y] if command_1[y] > command_2[y] else command_2[y] for y in range(20)]
print('Первая команда: ',command_1)
print('Вторая команда: ',command_2)
print('Победители тура: ',champions)