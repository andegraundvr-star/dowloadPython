#Член семьи
family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
#создание структуры из информации словарей с данными
new_structure = (
    family_member['name'],
    family_member['surname'],
    family_member['hobbies'],
    family_member['age'],
    family_member['children']
)
print('Кортеж с данными: ')
print(new_structure)
print()
#проверка списка словарей, какие значения принимают ключи name
print('Имена детей: ')
for child in family_member['children']:
        print(child['name'])
