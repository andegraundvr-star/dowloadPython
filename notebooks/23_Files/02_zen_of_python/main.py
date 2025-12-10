# Дзен Пайтона

#открываем файл для записи всех данных один раз
with open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\02_zen_of_python\zen.txt', 'r', encoding='utf-8') as file_zen:

    #т.к. в файле записана первая строка без переноса, читаем все строки, сохраняя оригинальные переносы
    lines = file_zen.readlines()

    #обрабатываем циклом строки и приводим к единообразию с одним переносом
    for i in range(len(lines)):
        if lines:
            if not lines[i].endswith('\n'):
                lines[i] = lines[i] + '\n'  #добавляем перенос для единообразия

    #циклом выводим в обратном порядке, пропуская пустые строки
    for line in reversed(lines):
        if line.strip():
            print(line, end='')  #добавляем end='' так как переносы уже есть в строках