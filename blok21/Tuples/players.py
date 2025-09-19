#Игроки
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
final_list = []
for i_key,i_value in players.items(): #создаем два списка из ключей и значений
    name_key = [x for x in i_key]
    rate_value = [y for y in i_value]
    final_tuple = tuple(name_key + rate_value) #конвертируем в кортеж
    final_list.append(final_tuple) #собираем кортежи в список
print(f"\nРезультат работы программы: ")
print(final_list)
