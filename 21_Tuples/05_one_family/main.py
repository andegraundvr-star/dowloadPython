#Одна семья
famaly = {
    ("Сидоров", "Никита"): '35',
    ("Сидорова", "Алина"): '34',
    ("Сидоров", "Павел"): '10'
}

target = input('Введите фамилию: ').lower() #переводим в нижний регистр
#удаляем окончание в фамилии женского рода
if target.endswith(('а')):
    target = target[:-1]

for i_key,i_value in famaly.items():
    #создаем переменную из двух дначений кортежа ключа словаря
    name_key = [x for x in i_key]
    #проверка на соответсвие фамилии из словаря с введенной фамилией
    if name_key[0].endswith(('а')):
        name_key[0] = name_key[0][:-1].lower() #переводим в нижний регистр
    if target == name_key[0]:
        #выводим ранее созданную переменную и значение словаря
        print(f"\nВ базе найдены данные по семье: ")
        for name_key, age_value in famaly.items():
            print(f"{' '.join(name_key)} -- {age_value}")

