# Кино
films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

your_films = []

redaction = input('хотите отредактировать ваш топ (да/нет)? ').lower()

while redaction == 'да':

    action = input('введите: добавить или удалить ').lower()
    if action == 'добавить':
        while True:
            point_out = input('укажите название фильма: ')
            if point_out not in films:
                print('вы не можете выбрать этот фильм, его нет в библиотеке ')
                continue
            if point_out in your_films:
                print('такой фильм уже есть в вашем списке ')
                continue
            position = int(input('на какую позицию претендует этот фильм? ')) - 1
            your_films.insert(position, point_out)
            print('фильм ',point_out,' добавлен на позицию ',position + 1)
            break
    elif action == 'удалить':
        point_out = input('укажите название фильма: ')
        if point_out not in your_films:
            print('такого фильма нет в вашем списке')
            continue
        your_films.remove(point_out)
        print('фильм ',point_out, 'удален из вашего списка')
    else:
        print('не верная команда. Используйте: добавить или удалить')
    redaction = input('Продолжить редактирование? (да/нет): ').lower()


print('Редактирование закончено, итоговый список: ',your_films)
