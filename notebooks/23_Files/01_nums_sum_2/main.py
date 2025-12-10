# Сумма чисел 2
#задаем путь, юникод
file = open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\01_nums_sum_2\numbers.txt', 'r', encoding='utf-8')
summ = 0
#проходим циклом по строкам файла, задаем условие: если символ первого с конца элемента скиска состоит из числа, производим вычисление
for i_line in file:
    # удаляем пробелы и \n в начале и конце строки
    i_line = i_line.strip()
    # проверяем, что строка не пустая и последний символ — цифра
    if i_line and i_line[-1].isdigit():
        summ += int(i_line)
    else:
        continue
#закрываем файл
file.close()
print("summ",summ) #вывод не обязателен
#открываем новый файл для записи, ипользуем w
to_file = open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\01_nums_sum_2\answer.txt', 'w', encoding='utf-8')
to_file.write(f"{summ}")#записываем summ в виде строки
file.close()#закрываем файл
