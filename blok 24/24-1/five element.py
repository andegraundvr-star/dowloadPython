# Пятый элемент
BRUCE_WILLIS = 42



input_data = input('Введите строку: ')


try:
    #пытаемся получить 5й символ (4й индекс) и преобразовать в число
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except IndexError:
    print("Ошибка: такого индекса нет в строке")
except ValueError:
    print("Ошибка: не верное значение символа")
except Exception as e:
    print("Ошибка: неверный формат ввода")
