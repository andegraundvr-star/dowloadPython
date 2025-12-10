# Ревью кода
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def stud(dict):
    lst = []
    cnt = 0
    pairs = []
    for i_id, i_info in dict.items():
        #добавляем пару (ID, возраст)
        pairs.append((i_id, i_info['age']))
        #добавляем интересы студента в общий список
        if 'interests' in i_info:
            lst.extend(i_info['interests'])
        #считаем длину фамилии
        cnt += len(i_info['surname'])

    return lst, cnt, pairs


#вызываем функцию
lst, cnt, pairs = stud(students)
#выводим результаты
print(f"\nСписок всех интересов:, {', '.join(lst)}")
print(f"\nОбщая длина всех фамилий: {cnt} символов")
#print(type(pairs))
print(f"\nСписок пар (ID студента, возраст):")
for student_id, age in pairs:
    print(f" {student_id} : {age}")