#Турнир

#Функция для получения балла из элемента словаря
def get_score(item):
    return item[1]  #возвращаем значение (балл)

#делаем функцию обработки списка первого файла
def process_tournament(file_path):
    #читаем все строки из файла
    with open(file_path, 'r', encoding='utf-8') as f:
        #создаем переменную список с разделением по переносам строк
        lines = [line.strip() for line in f if line.strip()]
        #print(lines)
    #если в файле нет такста, возвращаем пустой словарь
    if not lines:
        return {}

    #первая строка - минимальный проходной балл
    try:
        min_score = int(lines[0])
    #проверки на соответвие значения и наличие индекса списка, возврат - пустой словарь
    except (IndexError, ValueError):
        print("Ошибка: неверный формат файла")
        return {}
    #создание словаря с участниками
    participants = {}

    #обрабатываем участников (остальные строки)
    for line in lines[1:]:
        parts = line.split()
        if len(parts) < 3:
            continue

        last_name, first_name, score = parts[0], parts[1], parts[2]
        try:
            score = int(score)
        #если быллы не найдены, продолжаем
        except ValueError:
            continue
        #создаем условие попадания фамилий в словарь второго тура
        if score > min_score:
            #сохраняем словарь в формате фамилия, (только первый индекс с точкай от имени), балл
            participants[f"{last_name} {first_name[0]}."] = score

    #сортируем участников по убыванию баллов с использованием функции получения баллов из элемента словаря
    sorted_items = sorted(participants.items(), key=get_score, reverse=True)
    sorted_participants = dict(sorted_items)

    return sorted_participants

#функция перевода результатов в новый файл
def save_results(output_path, results):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"{len(results)}\n")
        for i, (name, score) in enumerate(results.items(), 1):
            f.write(f"{i}) {name} {score}\n")


#основной код
input_file = r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\07_tournament\first_tour.txt'
output_file = r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\07_tournament\second_tour.txt'

#обрабатываем турнир
results = process_tournament(input_file)

#сохраняем результаты
save_results(output_file, results)

#выводим информацию
print(f"Обработано участников: {len(results)}")
print("Результаты сохранены в:", output_file)