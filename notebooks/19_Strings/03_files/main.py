#  Файлы
file_name = input('Введите название файла: ') #@example.txt
#задаем форматирование строки
path = '{name}'.format(name = file_name.lower())
#print('Название файла: ',path)
#вводим первое условие на проверку расширений
if path.lower().endswith('.txt') or path.lower().endswith('.docx'):
    print('Расширение фала соответствует нормативу')
else:
    print('Расшерение файла не установленного образца, замените')
#вводим второе условие на проверку допустимых символов
error_symbols = '@№$%^&*()'  # Запрещённые символы
if any(path.startswith(symbol) for symbol in error_symbols):
    print('Ошибка: имя файла содержит запрещённый символ в начале')
else:
    print('Наименование файла соответствует нормативу')
