# Разворот
sequence = input('введите последовательность с двумя символами h: ')
#вводим две переменные .в которые записываются индексы первого и последнего символа "h"
count = 0
count_2 = 0
#находим первый индекс символа "h"
for i in sequence:
    count +=1
    if i == 'h':
        break
#находим последний индекс символа "h" с помощью обратного цикла
for j in sequence[::-1]:
    count_2 += 1
    if j == 'h':
       break
#print('count',count)
#print('count_2',count_2)
#print(len(sequence))
#с помощью срезов записываем в пеерменые необходимые части данной строки
idx = sequence[:count]
idx_2 = sequence[len(sequence)-count_2:]
#print('idx',idx)
#print('idx_2',idx_2)
idx_3 = sequence[count:len(sequence)-count_2][::-1]
#складываем полученные части строки
print('измененная строка: ',idx + idx_3 + idx_2)