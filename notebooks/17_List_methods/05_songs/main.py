#Песни
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_list = ['',0]
distance = 0
sum_song = int(input('сколько песен нужно переместить? '))

for song_name, distance in violator_songs:
    for i in range(sum_song - 1):
        print('укажите название',i + 1,' песни: ', end='')
        song_name = input()
        new_list.append(song_name)
        if song_name in violator_songs:
            distance += distance
print('Обновленный список песен:')
for idx in new_list:
    print('назвение',idx, 'песни', new_list[idx])
print('Общее время звучания песен: ', distance)
