# Протокол соревнований
import random
N = random.randint(3,9)
print(f"Текущее количество участиков в игре: {N}")
storageOfName = "jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley", "barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers",
"warren", "keller"
#создаем списки рандомных учатников и переменную рандомного количества очков
tournamentPoints = random.randint(599,999)
tournamentPlayers = [random.choice(storageOfName) for x in range(1,N +1)]
#nickName = random.choice(storageOfName)
#print(tournamentPlayers)

playerPoints = {}
#добавляем участников и их очки в словарь
for i, name in enumerate(tournamentPlayers, 1):
    points = random.randint(599, 999)
    playerPoints[i] = (points, name)  #номер записи: (имя, очки)
print(f"\nЗаписи протокола (результат и имя):")
#выводим изначальный словарь протоколов
for i, (points, name) in playerPoints.items():
    print(f"{i} запись: {points} {name}")
#print(playerPoints)

#преобразуем в список кортежей (очки, имя, исходный номер)
temp_list = [(points, name, i) for i, (points, name) in playerPoints.items()]
#сортируем по первому элементу (очкам)
temp_list.sort(reverse=True)
#берем топ-3 и преобразуем в список кортежей
sorted_results = [(i, (points, name)) for points, name, i in temp_list[:3]]
#print(sorted_results)
#выводим конечный обработанный список
print("\nРезультаты турнира (топ 3):")
for position, (i, (points, name)) in enumerate(sorted_results, 1):
    print(f"{position} место. {name} ({points})")
