#  Самое длинное слово
#сразу преобразуем строку в список
start_line = input('введите строку: ').split()
print(start_line)
maximum = []
target = 0
#находим в списке максимально длинное слово
for i in start_line:
    digits = str(i)
    maximum.append(len(digits))
#сравниваем каждое слово этого списка с мксимально длинным и выходим из цикла
for i in start_line:
    digits = str(i)
    if max(maximum) == len(digits):
        print(i)
        print(max(maximum))
        break



