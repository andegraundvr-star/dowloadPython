# Анализ слова 2
left_new_page = []
rigth_new_page = []
count_i = 0
count_Ri = 0
line = input('введите слово: ')
#print(len(line))
for i in line:
    count_i += 1
    left_new_page.append(i)
    if count_i == len(line) // 2:
        break
#print(left_new_page)

for i in range(len(line) - 1, -1, -1):
    count_Ri += 1
    rigth_new_page.append(line[i])
    if count_Ri == len(line) // 2:
        break
#print(rigth_new_page)
if left_new_page == rigth_new_page:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

