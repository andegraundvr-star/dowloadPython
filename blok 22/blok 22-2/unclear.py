#Непонятно!
object = {"a": 10, "b": 20}

print(f'object = "{object}"')
print(f"\nТип данных: {type(object)}", end='')

if isinstance(object, str):
    print(" (строка)")
    print(f"\nНеизменяемый (immutable)")
elif isinstance(object, int):
    print(" (целые числа)")
    print(f"\nНеизменяемый (immutable)")
elif isinstance(object, bool):
    print(" (булевы значения)")
    print(f"\nНеизменяемый (immutable)")
elif isinstance(object, float):
    print(" (числа с плавающей точкой)")
    print(f"\nНеизменяемый (immutable)")
elif isinstance(object, tuple) or isinstance(object, range):
    print(" (последовательности)")
    print(f"\nНеизменяемый (immutable)")  #кортежи и range неизменяемы
elif isinstance(object, list):
    print(" (списки)")
    print(f"\nИзменяемый (mutable)")
elif isinstance(object, dict):
    print(" (словари)")
    print(f"\nИзменяемый (mutable)")
elif isinstance(object, set):
    print(" (множества)")
    print(f"\nИзменяемый (mutable)")  #множества изменяемы
elif isinstance(object, frozenset):
    print(" (неизменяемые множества)")
    print(f"\nНеизменяемый (immutable)")

print(f"\nid объекта: {id(object)}")
print()
print("Неизменяемые (immutable): int, float, bool, str, tuple, range, frozenset")
print("Изменяемые (mutable): list, dict, set")
