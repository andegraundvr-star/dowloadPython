#  Года
def has_three_identical_digits(number):
    digits = str(number)
    for digit in digits:
        if digits.count(digit) == 3:
            return True
    return False

def main():
    while True:
        A_str = input("Введите первый год: ")
        B_str = input("Введите второй год: ")

        if len(A_str) != 4 or len(B_str) != 4:
            print("Ошибка: число должно содержать ровно 4 цифры. Попробуйте снова.")
            continue

        if not (A_str.isdigit() and B_str.isdigit()):
            print("Ошибка: вводить можно только цифры. Попробуйте снова.")
            continue

        A = int(A_str)
        B = int(B_str)
        break

    if A > B:
        A, B = B, A

    print('Года от ',A,' до ',B,' с тремя одинаковыми цифрами:')

    found = False
    for number in range(A, B + 1):
        if has_three_identical_digits(number):
            print(number)
            found = True

    if not found:
        print("В заданном диапазоне нет значений с ровно тремя одинаковыми цифрами.")
main()
