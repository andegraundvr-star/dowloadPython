# Поиск элемента 2

site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

#создаем функцию поиска ключа в словаре
def find_key(data, key, current_level=1, max_level=None):
    #вводим ограничение при нахождении ключа
    if key in data:
        return data[key]
    #вводим ограничение по уровню вложенности
    if max_level and current_level >= max_level:
        return None
    #добавляем цикл перебора значений словаря
    for value in data.values():
        #проверка каждого значения словаря на тип - словарь
        if isinstance(value, dict):
            #создание рекурсии, вызов функции для вложенного словаря, передача на вход ключ и и ограничение max_level
            result = find_key(value, key, current_level + 1, max_level)
            #если во вложенном словаре найден ключ, функция возвращает найденное значение
            if result is not None:
                return result
    #возврат none в случае отвуствия ключа во всем словаре
    return None

#создаем функцию для обработки данных ввода
def target():
    while True:
        #ввод первого позиционного аргумента
        key_name = input("Введите имя ключа: ").lower()
        #условие выхода при пустом вводе
        if not key_name:
            break
        #ввод значений второго аргумента
        level_input = input("Введите максимальный уровень вложенности (Enter - без ограничений): ")
        #задание максимального уровня поиска, присвоение значение None при пустом вводе
        max_level = int(level_input) if level_input else None
        #применение функции по поиску ключа с вводом первого, второго позиционного агрумента и третьего аргумента по умолчанию
        result = find_key(site, key_name, max_level=max_level)
        #условия для вывода при нахождении ключа на заданном уровне и при отсутствии
        if result is not None:
            print(f"Значение ключа '{key_name}': {result}")
        else:
            print(f"Ключ '{key_name}' не найден")


target()