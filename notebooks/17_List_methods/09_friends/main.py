# Друзья
N = int(input('введите количество друзей: '))
K = int(input('введите количество долговых расписок: ' ))

print('количество друзей: ',N)
print('количество расписок: ',K)

final_calculation = [0] * N

for i in range(K):
    print('\n',i + 1, 'расписка ')
    creditor = int(input('Кому должны деньги (номер друга): ')) - 1
    debtor = int(input('Кто должен деньги (номер друга): ')) - 1
    cache = int(input('Сумма долга: '))
    final_calculation[debtor] -= cache
    final_calculation[creditor] += cache

print('\nБаланс друзей:')
for i in range(N):
    print(i + 1,' Друг: ',final_calculation[i])
