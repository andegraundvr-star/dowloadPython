nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# Список списков 2
def summ_does_no_metter_that(object):
    simple_list = []
    if isinstance(object, (list, tuple, set)):
    # перебираем список, если находим список, множество или кортеж, создаем рекурсию
        for low_object in object:
            simple_list += summ_does_no_metter_that(low_object)
    # если находим словарь, то создаем рекурсию
    elif isinstance(object, dict):
        for value in object.values():
            simple_list += summ_does_no_metter_that(value)
    #если можно сложить, добавляем в список
    elif isinstance(object, (int, float)):
        simple_list.append(object)

    return simple_list
#выводим условие и результат вычисления
print(f"List: {nice_list}")
print(f"Ответ: {summ_does_no_metter_that(nice_list)}")
