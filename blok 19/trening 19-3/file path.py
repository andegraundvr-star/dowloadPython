#Путь к файлу
format = input('введите расширение файла: ')
disc = input('введите имя диска, на котором лежит файл: ')
#формируем путь (приводим диск к нижнему регистру при создании пути)
path = '{C}:/user/docs/folder/new_file.{txt}'.format(
C = disc.lower(),
txt = format)
print('Путь к файлу: ',path)
#проверяем условия (используем lower() для регистронезависимой проверки)
if path.lower().endswith('.txt') and path.lower().startswith('c:/'):
    print('расширение и расположение соответствует')
    print('на каком диске должен лежать файл: C')
    print('требуемое расширение файла: .txt')
else:
    print('ошибка')


