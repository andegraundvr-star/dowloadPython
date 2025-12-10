#Кратность
nums_list = []
new_list = []
summ_idx = 0
N = int(input('Кол-во чисел в списке: '))
for i in range(N):
    print('введите', i + 1,' число: ', end = '')
    numerator = int(input())
    numerator = nums_list.append(numerator)

denominator = int(input('введите делитель: '))

for index in range(N):
    if nums_list[index] % denominator == 0:
        new_list.append(index)
        summ_idx += index
        print('индекс числа ',nums_list[index],':', index)

print('сумма индексов равна: ', summ_idx)