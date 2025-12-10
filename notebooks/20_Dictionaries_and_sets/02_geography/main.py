# География
N = int(input('введите количество стран: '))
#создаем цикл для добавления в словарь стран - ключей и списков городов - значений
country_dict = dict()
for i in range(N):
    country_list = input('Введите страну и города через пробел: ').split()
    country = country_list[0]
    cities = country_list[1:]
    country_dict[country] = cities

print('\nСозданный словарь:')
for i in country_dict:
    print(f'{i} - {country_dict[i]}')

#реалицация цикла для поиска стран по названию городов

for _ in range(3):
    city = input('\nВведите город для поиска страны: ')
    found = False
    for country, cities in country_dict.items():
        if city in cities:
            print(f'Город {city} расположен в стране {country}')
            found = True
            break

    if not found:
        print(f'По городу {city} данных нет.')