#очень простая задача
people_on_work = []
personal = int(input('количество сотрудников в офисе: '))
for _ in range(personal):
    id_worker = int(input('введите ИД сотрудника: '))
    people_on_work.append(id_worker)
target_worker = int(input('какой ИД ищем? '))
for id in people_on_work:
    if id == target_worker:
        print('сотрудник на работе')
        break
    else:
        print('сотрудник не работает')
        break

