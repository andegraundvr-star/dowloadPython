#олимпиада
n = int(input('количество учатсников: '))
m = int(input('количество человек в команде: '))
list_of_persons = []
nom = 1
if n % m != 0:
    print(n, 'участников невозможно поделить на команды по ',m,'человек')
    #print(n // m)
else:
    for i in range(n // m):
        list_of_persons.append(list(range(nom, nom + m)))
        nom = nom + m
    print('общий список команд ',list_of_persons)
