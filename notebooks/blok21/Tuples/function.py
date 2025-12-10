#Функция
input_values = input('Введите кортеж (значения через запятую): ').split(',')
start_tuple = tuple(value.strip() for value in input_values)
random_element = input('Введите элемент: ').strip()


def filter_tuple(input_tuple, element):
    indices = [i for i, x in enumerate(input_tuple) if x == element]
    if not indices:
        return tuple()  #элемент не найден
    elif len(indices) == 1:
        #возвращаем от первого вхождения до конца
        return input_tuple[indices[0]:]
    else:
        #возвращаем от первого до второго вхождения включительно
        return input_tuple[indices[0]:indices[1] + 1]

#вызов функции
result = filter_tuple(start_tuple, random_element)
#print(type(result))
print(f"Результат: {result}")

