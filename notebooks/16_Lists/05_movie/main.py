films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# Кино
favorite_movie = []
for idx_l in range(len(films)):
    print('напишите название любимого фильма или "end" для выхода: ', end = '')
    like = input()
    if like == 'end':
        break
    else:
        for idx_c in films:
            if idx_c == like:
                favorite_movie.append(idx_c)

print('итоговый список любимых фильмов: ',favorite_movie)