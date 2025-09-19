# Считалка
N = int(input('введите количество человек: '))
K = int(input('какой номер на выбивание? ' ))

print('значит выбывает каждый',K,' человек')
circle = list(range(1, N + 1))
print('текущий круг людей: ',circle)
start = 0
print('начало старта: ',start + 1)
people_index = N
leave = ''
prirost = 0

while people_index > 1:
    if start + K > len(circle):
        circle.extend(circle)
        #print(circle)
        prirost +=1
    i = 1
    for i in range(start, len(circle)):
        original_circle = []

        while i == K:

            people_index -=1
    #    if i == str(K):
            #print(circle[i])
            leave = circle[i]
            print('выбывает игрок номер: ', circle[i])
            while leave in circle:
                circle.remove(leave)

            for j in range(people_index):  #
                original_circle.append(circle[j])
            #print(circle)

            print('текущий круг людей: ',original_circle)
            if people_index > 1:
                print('начало отчета с номера: ',circle[i] - 1)
            else:
                print('остался один участник под номером: ', circle[j])
            start = leave

            break



