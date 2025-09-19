# Продвинутая функция sum
iter_object = (1, 2, 3, 4, 5)
def summ_does_no_metter_that(object):
    sum_num = 0
    if isinstance(object, (list, tuple, set)):
        #перебираем список, если находим список, множество или кортеж, создаем рекурсию
        for low_object in object:
            sum_num += summ_does_no_metter_that(low_object)
    #если находим словарь, то создаем рекурсию
    elif isinstance(object, dict):
        for value in object.values():
            sum_num += summ_does_no_metter_that(value)
    #если можно сложить, делаем сумму
    elif isinstance(object, (int, float)):
        sum_num += object
    return sum_num
#выводим условие и результат вычисления
print(f"Sum: {iter_object}")
print(f"Ответ: {summ_does_no_metter_that(iter_object)}")


