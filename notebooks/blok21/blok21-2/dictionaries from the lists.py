#Словари из списков
#создаем два списка и два пустых словаря
line_1 = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
print(f"\nПервый список: {line_1}")
line_2 = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
print(f"\nВторой список: {line_2}")
dict_1 = dict()
dict_2 = dict()
#циклом и функцией enumerate вносим в словари ключи и значения из списков
for idx, value in enumerate(line_1):
    dict_1[idx] = value
for idx, value in enumerate(line_2):
    dict_2[idx] = value
#выводим словари
print(f"\nПервый словарь: {dict_1}")
print(f"\nВторой словарь: {dict_2}")
