violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# Песни 2
print(f'Доступные песни для добавления: ')
for i,(song) in enumerate(violator_songs):
    print(f'{i+1} песня: {song}')
#создаем список порядковых номеров песен для добавления
text = input('введите порядковые номера песен через пробел, которые необходимо добавить в ваш плей-лист: ').split(' ')

#преобразуем номера в индексы (отнимаем 1) и убираем дубликаты
new_text = set(int(num)-1 for num in text if num.isdigit())
#print(new_text)
#создаем список всех песен для доступа по индексу
songs_list = list(violator_songs.items())
#print(songs_list)
#добавляем выбранные песни в новый словарь
my_play_dict = dict()
for idx in new_text:
    if 0 <= idx < len(songs_list):
        song, duration = songs_list[idx]
        my_play_dict[song] = duration
#выводим новый список песен на экран с помощью цикла
print('\nВаш новый плей-лист:')
for song, duration in my_play_dict.items():
    print(f'{song}: {duration}')

#выводим общую длительность выбранных треков
total_duration = sum(my_play_dict.values())
print(f'\nОбщая длительность: {round(total_duration, 2)} минут')
