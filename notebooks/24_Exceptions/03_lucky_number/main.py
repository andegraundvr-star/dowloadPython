#счастливый номер
import random
import os

#задаем путь к файлам
base_dir = r"C:\Root\RemoteFolders\user0907"
output_path = os.path.join(base_dir, 'python-ds', '24_Exceptions', '03_lucky_number')
output_file = os.path.join(output_path, 'lucky.txt')

lucky_number = random.randint(1, 13)

#функция случайных исключений
def raise_exception(number):
    exceptions = {
        1: 'не летная погода',
        2: 'високосный год',
        3: 'вспышки на солнце',
        4: 'встали не с той ноги',
        5: 'не в мою смену',
        6: 'позвоните маме',
        7: 'перезапустите завтра',
        8: 'попробуйте другой браузер',
        9: 'перезагрузите компьютер',
        10: 'переустановите винду',
        11: 'заплатите налоги',
        12: 'погладь кота',
        13: 'введите капчу'
    }

    if number not in exceptions:
        raise ValueError("Номер исключения должен быть от 1 до 13")

    raise Exception(exceptions[number])

print(f"Счастливое секретное число: {lucky_number}")

sum_num = 0
numbers = []  #будем сохранять все введенные числа

try:
    for i in range(1, 778):  #от 1 до 777 включительно
        try:
            input_number = int(input('Введите любое целое число: '))
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        sum_num += input_number
        numbers.append(str(input_number))

        if sum_num > 777:
            print(f"Сумма превысила 777! Текущая сумма: {sum_num}")
            break

        print(f"Вы ввели: {input_number}")

        if i == lucky_number:
            try:
                raise_exception(lucky_number)
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break

    #cохраняем все числа в файл один раз в конце
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(numbers))
        print(f"Все числа сохранены в файл: {output_file}")

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")