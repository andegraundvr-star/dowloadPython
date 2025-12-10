#Вечеринка
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
command = ' '
print('сейчас на вечеринке', len(guests),'человек : ',guests)
while command != 'вечеринка закончена':
    command = input('гость пришел, ушел или вечеринка закончена? ')
    if command =='пришел':
        name = input('кто пришел? ')
        if len(guests) >= 6:
            print('sorry, ',name,' , мест сейчас нет')
        else:
            print('привет ',name,'!')
            guests.append(name)
            print('сейчас на вечеринке', len(guests), 'человек : ', guests)
    elif command == 'ушел':
        name = input('кто ушел? ')
        if name not in guests:
            print('такого гостя нет сейчас с нами')
        else:
            guests.remove(name)
            print('до свидания, ',name)
            print('сейчас на вечеринке', len(guests), 'человек : ', guests)

print('вечеринка окончена, все спят')

