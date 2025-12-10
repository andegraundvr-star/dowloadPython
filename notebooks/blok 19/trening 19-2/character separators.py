#Разделители символов
#по условию вводим строку поздравления, список именнинников и строку возрастов
while True: #добавляем контроль воода
    pattern = input('введите шаблон поздравления (подставить вместо имени и возраста: {name} и {age}): ')
    if '{name}' in pattern and '{age}' in pattern:
        break
    print('введите обязательные конструкции: {name} и {age}')
persons = input('введите ИО именинников через ",": ').split(', ')
while True: #добавляем контроль воода
    ages_str = input('введите возраст каждого человека (в одну строку через пробел): ')
    if len([int(x) for x in ages_str.split()]) == len(persons):
        break
    print('введите количество возрасов через пробел равное количеству имен')
#переводим строку возрастов в список
ages = [int(x) for x in ages_str.split()]
#через цикл выводим сами поздравления
for i in range(len(persons)):
    print(pattern.format(name=persons[i],age=ages[i]))
#собираем список именинников с возрастами
people = [' '.join([persons[i],str(ages[i])]) for i in range(len(persons))]
#переводим список в строку
people_str = ', '.join(people)
print('\nименинники: ',people_str)