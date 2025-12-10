# Сумма и разность
nomber = int(input('Введите число: '))
def summ(nomber):
    num_sum = 0
    while nomber != 0:
        lost_nomber = nomber % 10
        num_sum += lost_nomber
        nomber //= 10
    #print('num', nomber, 'print', num_sum)
    return num_sum
summ(nomber)
def count(nomber):
    count_nomber = 0
    while nomber != 0:
        lost_nomber = nomber % 10
        count_nomber += 1
        nomber //= 10
    return count_nomber

count(nomber)
print('сумма чисел: ', summ(nomber))
print('количество цифр: ', count(nomber))
print('Разность суммы и кол-ва цифр: ',summ(nomber) - count(nomber))
