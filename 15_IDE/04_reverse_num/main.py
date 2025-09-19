# Число наоборот 3
first_n = float(input("Введите первое число: "))
second_n = float(input("\nВведите второе число: "))
def transformation():
    num_str = str(first_n)
    integer_part = ""
    fractional_part = ""
    dot_found = False

    for char in num_str:
        if char == '.':
            dot_found = True
        elif not dot_found:
            integer_part += char
        else:
            fractional_part += char

    revers_integer_part = str()
    for i in integer_part[::-1]:
        revers_integer_part = revers_integer_part + i

    revers_fractional_part = str()
    for i in fractional_part[::-1]:
        revers_fractional_part = revers_fractional_part + i

    float_number_one = float(str(revers_integer_part) + "." + str(revers_fractional_part))
    return float_number_one # 321.654
float_number_one = transformation()

def transformation_two():
    num_str = str(second_n)
    integer_part = ""
    fractional_part = ""
    dot_found = False

    for char in num_str:
        if char == '.':
            dot_found = True
        elif not dot_found:
            integer_part += char
        else:
            fractional_part += char

    revers_integer_part = str()
    for i in integer_part[::-1]:
        revers_integer_part = revers_integer_part + i

    revers_fractional_part = str()
    for i in fractional_part[::-1]:
        revers_fractional_part = revers_fractional_part + i

    float_number_two = float(str(revers_integer_part) + "." + str(revers_fractional_part))
    return float_number_two # 321.654

float_number_two = transformation_two()
print('первое число наоборот: ',float_number_one)
print('второе число наоборот: ',float_number_two)
print('сумма:', float_number_one + float_number_two)




