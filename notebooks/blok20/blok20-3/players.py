#Игроки
players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}
#Все члены команды из команды А, которые отдыхают.
comand_A = [x['name'] for x in players_dict.values() if x['team'] == 'A' and x['status'] == 'Rest']
print('Все члены команды из команды А, которые отдыхают: ',comand_A)
#Все члены команды из группы B, которые тренируются.
comand_B = [x['name'] for x in players_dict.values() if x['team'] == 'B' and x['status'] == 'Training']
print('Все члены команды из группы B, которые тренируются: ',comand_B)
#Все члены команды из команды C, которые путешествуют.
comand_C = [x['name'] for x in players_dict.values() if x['team'] == 'C' and x['status'] == 'Travel']
print('Все члены команды из команды C, которые путешествуют: ',comand_C)
