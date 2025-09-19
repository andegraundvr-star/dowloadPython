#Соседи
neighbors = input('введите строку: ')
symbol = int(input('введите номер символа: '))
sum_list = []

count = 0
summ_idx = 0

for sim in neighbors:
    sum_list.append(sim)

print('выбран символ: ', sum_list[symbol - 1])
print('соседями этого символа являются: ', sum_list[symbol - 2],'и', sum_list[symbol])

found =  sum_list[symbol - 2] + sum_list[symbol - 1] + sum_list[symbol]

duplicate_positions = []
for i in range(len(neighbors)):
    new_pos = neighbors[i]
    if new_pos == sum_list[symbol - 1]:
        duplicate_positions.append(i + 1)
print('выбранный символ встречается на следующих позициях в строке: ', duplicate_positions)

count_k = 0
for k in range(len(duplicate_positions)):
    count_k += 1
#print('k = ',count_k )
if count_k == 1:
    print('совпадений комбинаций выявлено')
elif count_k > 1:
    for i in range(count_k):
        duplicate_found = sum_list[duplicate_positions[i] - 2] + sum_list[duplicate_positions[i] - 1] + sum_list[duplicate_positions[i]]
        #print(found)
        #print(duplicate_found)
        if found == duplicate_found:
            count += 1
    if count == 2:
        print('есть ровно один такой же набор символов', found)
    else:
        print('количество наборов символов',found,'составляет', count)

