#Результаты
#задаем путь, юникод
file = open(r'C:\Root\RemoteFolders\user0907\Мои документы\task\group_1.txt', 'r',encoding='utf-8')
summa = 0
#проходим циклом по строкам файлов, делим строки на список объектов по разделителю пробел
for i_line in file:
    info = i_line.strip().split()
    #задаем условие: если символ первого с конца элемента скиска состоит из числа, производим вычисление
    if info and info[-1].isdigit():
        summa += int(info[-1])
#закрываем файл
file.close()

file = open(r'C:\Root\RemoteFolders\user0907\Мои документы\task\group_1.txt', 'r',encoding='utf-8')
diff = 0
for i_line in file:
    info = i_line.strip().split()
    if info and info[-1].isdigit():
        diff -= int(info[-1])
file.close()

file_2 = open(r'C:\Root\RemoteFolders\user0907\Мои документы\task\additinal_into\group_2.txt', 'r',encoding='utf-8')
compose = 1
for i_line in file_2:
    info = i_line.strip().split()
    if info and info[-1].isdigit():
        compose *= int(info[-1])
file_2.close()


print("summa",summa)

print("diff",diff)

print("compose",compose)
