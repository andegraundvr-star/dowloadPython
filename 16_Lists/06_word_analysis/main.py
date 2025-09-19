# Анализ слова

build = []
text = input('введите слово: ')
for i in text:
    if i not in build:
        build.append(i)

print('количество уникальных знаков в слове: ',len(build))

