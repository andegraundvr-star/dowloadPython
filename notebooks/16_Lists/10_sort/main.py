# Сортировка
running_line = []
skip_next = False
target_pos_10 = -1
line = input('введите строку: ')

for i in range(len(line)-1):
    if line[i] == '1' and line[i+1] == '0':
        target_pos_10 = i
        break
i = 0
while i < len(line):
    if skip_next:
        skip_next = False
        i += 1
        continue

    if line[i] == '-':
        if i + 1 < len(line):
            running_line.append('-' + line[i + 1])
            skip_next = True
    elif i == target_pos_10:
        running_line.append('10')
        skip_next = True
    else:
        running_line.append(line[i])
    i += 1

print('изначальный список', running_line)

for i in range(len(running_line)):
    i = i
    min_idx = i
    for j in range(i + 1, len(running_line)):
        j = j
        if int(running_line[j]) < int(running_line[min_idx]):
            min_idx = j

    if int(min_idx) != int(i):
        running_line[i], running_line[min_idx] = running_line[min_idx], running_line[i]
print('отсортированный список', running_line)



