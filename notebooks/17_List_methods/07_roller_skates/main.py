# Ролики
N_shoes = int(input('введите количчество коньков: '))
N_people = int(input('введите количчество людей: '))
list_shoes = []
list_people =[]
for i in range(N_shoes):
    print('размер',i + 1,'пары: ', end = '')
    size = input()
    list_shoes.append(size)

new_list_shoes = list_shoes
for i in range(N_people):
    print('размер ноги',i + 1,'человека: ', end = '')
    leg = input()
    list_people.append(leg)
    #print(len(list_people))

count_happy_people = 0
shoe_index = 0

list_shoes.sort()
list_people.sort()

for leg in list_people:
    while shoe_index < len(list_shoes):
        if list_shoes[shoe_index] >= leg:
            count_happy_people += 1
            shoe_index += 1
            break
        shoe_index += 1
    else:
        break
print('\nсписок размеров коньков', list_shoes)
print('список размеров ног', list_people)
print('Наибольшее кол-во людей, которые могут взять ролики: ',count_happy_people)

