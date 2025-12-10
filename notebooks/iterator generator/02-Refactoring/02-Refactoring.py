#Рефакторинг
"""После различных вопросов про различия итераторов, генераторов и генераторных выражений на собеседовании вам дали небольшой пример кода и попросили «провести рефакторинг». Вот сам код:

# Нужно найти, какие два числа из списков в результате попарного перемножения дадут число 56.
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break

Проблема кода состоит в некрасивом выходе из циклов (два break и флаг). Реализуйте более красивый выход из циклов, используя генератор. Сам алгоритм решения (попарное перемножение) и списки трогать нельзя."""
#условие
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
can_continue = True
#функция-генератор
def squares_generator():
    for x in list_1:
        for y in list_2:
            yield x * y
#cоздаем генератор
gen = squares_generator()
#вывод
while can_continue:
    try:
        result = next(gen)
        #print(result)  #выводим текущий результат
        if result == to_find:
            print(result, 'Found!!!')#выводим требуемый результат
            break
    #когда значения закончились
    except StopIteration:
        print("Поиск завершен")
        can_continue = False
