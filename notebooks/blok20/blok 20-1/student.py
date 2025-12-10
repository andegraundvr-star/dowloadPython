#Студенты
info = input('введите информацию о студенте через пробел: ').split()
#print(info)
#создаем словарь
student = dict()
student['имя'] = info[0]
student['фамилия'] = info[1]
student['город'] = info[2]
student['ФУЗ'] = info[3]
student['оценки'] =[]
#циклом прописываем оценки в список на позиуию оценки в словаре
for i in info[4:]:
    student['оценки'].append(int(i))
#print(student)
#результат делавем циклом ключ - значение
print('результат:',end='')
for i in student:
    print(f'{i} - {student[i]}')