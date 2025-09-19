# Угадай число
import random
N = int(input('введите максимальное число: '))
sekter_nomber = random.randint(1,N)
#print(sekter_nomber)
inter = set()
possible_numbers = set()
for i in range(1, N + 1):
    possible_numbers.add(i)
#добавляем бесконечный цикл запросов чисел в виде списка
print(f'введите несколько числел через пробел! ')
while True:
    #если ввели стоп слово - заканчиваем програму
    add_nomber = input('\nНужное число есть среди вот этих чисел? ')
    if add_nomber.lower() in ['помогите', 'памагити', 'помогите!']:
        #выводим числа из множества через зяпятую
        print(f'Артём мог загадать следующие числа: {', '.join(map(str,possible_numbers))}')
        break
    #переводим введенные числа в нужный формат
    inter= set(map(int, add_nomber.split()))
    #print(inter)
    if sekter_nomber in inter:
        print('Ответ Артёма: Да')
        possible_numbers.intersection_update(inter)
        #задаем условия, если угадали число
        if len(add_nomber.split()) == 1 and sekter_nomber in inter:
            print(f'Вы победили! Загаданное число: {sekter_nomber}')
            break
    else:
        #оставляем в множестве возможных чисел только те, которые не называли
        print('Ответ Артёма: Нет')
        possible_numbers.difference_update(inter)


