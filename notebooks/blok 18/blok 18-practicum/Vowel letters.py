#Гласные буквы
password = input('введите строку: ')
#база гласных букв
vowel = 'аиеоюуыэя'
#vowel = [x for x in vowel]
#password = [y for y in password]
#удаляем гласные буквы из строки
new_password = [z for z in password if z in vowel]
print('список без гласных', new_password)
print('количество гласных в оставшейся строке:', len(new_password))