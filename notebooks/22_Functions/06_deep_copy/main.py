#Глубокое копирование
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

#создаем функцию замены значений в словаре
def replace_in_dict(data, old_words, new_words):
    if isinstance(old_words, str):
        #создаем список слов для замены
        old_words = [old_words]
    #если значение словаря строка, меняем значение на значение переменной
    for key, value in data.items():
        if isinstance(value, str):
            #перебираем список и меняем второй позиционный аргумент в словаре
            for word in old_words:
                value = value.replace(word, new_words)
            data[key] = value
        #если значение - словарь, создаем рекурсию для дальнейшей обработки
        elif isinstance(value, dict):
            replace_in_dict(value, old_words, new_words)
    return data

#создаем функцию для обработки данных ввода названий новых объектов
def generate_sites():
    #список сайтов компактных сайтов и их количество, введенное пользователем
    sites = []
    many_sites = int(input('Введите количество сайтов: '))

    for i in range(many_sites):
        new_title = input(f'Введите название товара для сайта №{i + 1}: ')

        #создаем глубокую копию шаблона
        import copy
        new_site = copy.deepcopy(site)

        #заменяем ключевые слова
        updated_site = replace_in_dict(new_site, "телефон", new_title)
        updated_site = replace_in_dict(new_site, "iphone", new_title)
        #добавляем измененный сайт в список сайтов
        sites.append(updated_site)
        #выводим название сайта и сам сайт с помощью созданной функции
        print(f'\nСайт для {new_title}:')
        print_site_compact(updated_site)

    return sites
#создаем функцию для вывода словаря на экран в первоначальном виде
def print_site_compact(site, indent=0):
    #создаем строку с пробелами и открывающейся скобки для отображения вложенности словаря
    indent_str = ' ' * indent
    print(indent_str + '{')
    #Выводим ключ в кавычках с отступом + 4 пробела
    for key, value in site.items():
        print(f"{indent_str}    '{key}': ", end='')
        #если значение является словарем, то запускаем рекурсию функции с добавлением еще 4х пробелов к отступу
        if isinstance(value, dict):
            print_site_compact(value, indent + 4)
        else:
            #если значение является строкой, то выводим её в кавычках
            print(f"'{value}'", end=',\n')
    #после обработки всех элементов словаря печатаем закрывающию скобку
    print(indent_str + '},')

#запускаем генерацию сайтов
generated_sites = generate_sites()