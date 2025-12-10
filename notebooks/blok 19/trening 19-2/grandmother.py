#Бабушка
import random
#сразу преобразуем строку в список
start_line = input('введите строку: ').split()
mem_list = []
true_list = []
#из списка выводим новую строку с пробелами, как требует условие

for i in start_line:
    mem_list.append(i)
    space = ' ' * random.choice(range(1, 11))
    mem_list.append(space)
result = ' '.join(mem_list)
print(result)
#заново избавляемся от пробелов через лист и далее строку
final_line = result.split()
true_frase = ' '.join(final_line)
print(true_frase)




