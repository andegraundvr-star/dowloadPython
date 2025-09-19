# Список списков 2
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

#разворачиваем двойную вложенность в один список
compleate_list = [z for x in nice_list
                   for y in x
                   for z in y]

print('ответ: ',compleate_list)
