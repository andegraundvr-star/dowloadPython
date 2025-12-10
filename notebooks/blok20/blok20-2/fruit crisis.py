#Кризис фруктов
incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}
#используем метод определения суммы
print(f'\nОбщий доход за год составил: {sum(incomes.values())} рублей')
#добавляем переменную, которая находит и отображает ключ словаря с минимальным значением
min_name = min(incomes, key=incomes.get)
print(f'\nсамый маленький доход у {min_name} , он составил: {min(incomes.values())} рублей')
#удаляем элемент из словаря по ключу
incomes.pop(min_name)
#выводим итоговый словарь
print(f'\nИтоговый словарь: {incomes}')
