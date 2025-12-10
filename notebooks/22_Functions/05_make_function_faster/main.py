
# Ускоряем работу функции

#создаем функцию со вторым аргументом по умолчанию

def calculating_math_func(data, fact={1: 1}):
    if data < 1:
        return 0  #создаем условие для остановки рекурсии
        #проверяем кеш перед вычислением
    if data not in fact:
        #создаем рекурсию и вычисляем факториал с сохранением результата в изменяемом типе данных - втором аргументе функции
        fact[data] = data * calculating_math_func(data - 1,fact)
    #извлечение значения из словаря в переменную
    factorial = fact[data]
    #выполняем остальные операции
    result = (factorial / (data ** 3)) ** 10
    return result

print(calculating_math_func(4))

