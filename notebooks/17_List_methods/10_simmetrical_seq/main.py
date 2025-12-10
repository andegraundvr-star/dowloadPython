# Симметричная последовательность
N = int(input('введите количество чисел в последовательности: '))
print('количество чисел: ',N)

sequence = []
for i in range(N):
    print('число',i + 1,': ', end='')
    nomber = input()
    sequence.append(nomber)

str_sequence = ''.join(sequence)
print('Последовательность:', ' '.join(sequence))

def is_symmetric(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if is_symmetric(str_sequence):
    print('Последовательность является симметричной')
else:
    for i in range(len(str_sequence)):
        symmetric = True
        left = i
        right = len(str_sequence) - 1
        while left < right:
            if str_sequence[left] != str_sequence[right]:
                symmetric = False
                break
            left += 1
            right -= 1

        if symmetric:
            numbers_to_add = []
            for j in range(i - 1, -1, -1):
                numbers_to_add.append(str_sequence[j])

            print('Нужно приписать чисел: ',i)
            print('Сами числа: ',' '.join(numbers_to_add))
            break
