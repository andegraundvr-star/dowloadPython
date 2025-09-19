# Сжатие
start_line = input('Введите строку: ')
compressed = []
count = 1

#считаем последовательные одинаковые символы
for i in range(1, len(start_line)):
    if start_line[i] == start_line[i-1]:
        count += 1
    else:
        compressed.append(start_line[i-1] + (str(count) if count > 1 else ''))
        count = 1

#добавляем последнюю последовательность
compressed.append(start_line[-1] + (str(count) if count > 1 else ''))

result = ''.join(compressed)
print('Закодированная строка: ',result)