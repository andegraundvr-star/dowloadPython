# Турнир
tournament_participants = []

for i in range(8):
    applicant = input('введите имя участника: ')

    if (i - 1)  % 2 != 0 and i > 0:
        applicant = tournament_participants.append(applicant)
print('участники с четным индексом', tournament_participants)
