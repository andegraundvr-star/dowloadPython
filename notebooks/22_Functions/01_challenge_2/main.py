# Challenge 2
N = int(input('Введите число: '))
def summation(num):
    #условия сотановки рекурсии
    if num == 0:
        return 0
    if num == 1:
        return 1
    # прибавляем вводимое значение на функцию от значения минус единица
    sum_num = num + summation(num - 1)
    return sum_num


result = summation(N)
print(f"Сумма всех чисел до числа {N}: {result}")



