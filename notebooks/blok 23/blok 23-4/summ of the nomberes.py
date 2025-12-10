#Сумма чисел
#задаем путь, юникод
file = open(r'C:\Root\RemoteFolders\user0907\Мои документы\task\nombers.txt', 'r',encoding='utf-8')
summa = 0
#проходим циклом по строкам файлов, задаем условие: если символ первого с конца элемента скиска состоит из числа, производим вычисление
for i_line in file:
    #удаляем пробелы и \n в начале и конце строки
    i_line = i_line.strip()
    #проверяем, что строка не пустая и последний символ — цифра
    if i_line and i_line[-1].isdigit():
        summa += int(i_line)

    else:
        continue
#закрываем файл
file.close()
print("summa",summa) #вывод не обязателен
#открываем новый файл для записи, ипользуем w
to_file = open(r'C:\Root\RemoteFolders\user0907\Мои документы\task\answer.txt', 'w',encoding='utf-8')
#записываем значение переменной summa (в виде строки + '\n' для переноса строки)
to_file.write(f"Сумма: {summa}\n")

file.close() #закрытие файла обязательно