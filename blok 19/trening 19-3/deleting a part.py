#Удаление части
#использование методов islower() и/или isupper()
path = input('Введите строку: ')
if path.islower() > path.isupper():
    path = path.lower()
    print(path)
else:
    path = path.upper()
    print(path)