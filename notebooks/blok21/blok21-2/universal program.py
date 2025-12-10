#Универсальная программа
print("Введите итерируемый объект: ", end='')
user_input = input().strip()

#если ввод пустой, считаем его пустой строкой
if not user_input:
    start_object = ""
else:
    #проверяем, является ли ввод строкой в кавычках
    if (user_input[0] == user_input[-1] and user_input[0] in ('"', "'")):
        start_object = user_input[1:-1]  #убираем кавычки
    #проверяем, похож ли ввод на список или кортеж
    elif user_input.startswith(('(', '[')) and user_input.endswith((')', ']')):
        #обработка списка/кортежа (без вложенных структур)
        elements = user_input[1:-1].split(',')
        if user_input.startswith('['):
            start_object = [elem.strip() for elem in elements]
        else:
            start_object = tuple(elem.strip() for elem in elements)
    else:
        start_object = user_input  #иначе оставляем как строку

#если объект не итерируемый, преобразуем в строку
if not isinstance(start_object, (list, tuple, str)):
    start_object = str(start_object)

result = [value for index, value in enumerate(start_object) if index % 2 == 0]
print(result)