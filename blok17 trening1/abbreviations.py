#Сокращения
state = int(input('количество работников '))
salary = []
count = 0
for i in range(state):
    payday = input('введите зарплату работника: ')
    salary.append(payday)
while '0' in salary:
    #print(salary)
    salary.remove('0')
for _ in salary:
    count +=1
print('осталось сотрудников: ',count)
print('обновленный список ЗП сотрудников', salary)
print('максимальная ЗП: ', max(salary))
print('минимальная ЗП: ', min(salary))