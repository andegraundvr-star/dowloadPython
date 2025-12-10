# Свой zip 2
def my_zip(*args):
    #используем map для передачи элементов каждого итератора как отдельные аргументы в лямбду
    return map(lambda *x: x, *args)

#берем объекты разной длинны
numbers = [1, 2, 3, 4]
letters = ('a', 'b', 'c')


#сохраняем результат в список для многократного использования
result = list(my_zip(numbers, letters))
#выводим списком
print(result)
#выводим отдельными элементами
for pair in result:
    print(pair)