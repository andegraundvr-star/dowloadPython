#Кубы и квадраты
left_border = int(input('введите начальное число: '))
right_border = int(input('введите конечное число: '))
#sequence = []
#for i in range(left_border, right_border + 1):
#    sequence.append(i)
#print(sequence)
#находим квадраты чисел в списке
quadro_sequence = [sequence ** 2 for sequence in range(left_border, right_border + 1)]
print('Список квадратов чисел в диапазоне от ',left_border,' до ',right_border,' : ',quadro_sequence)
#находим кубы чисел в списке
cub_sequence = [sequence ** 3 for sequence in range(left_border, right_border + 1)]
print('Список кубов чисел в диапазоне от ',left_border,' до ',right_border,' : ',cub_sequence)