def emulate_for(iterable):
    iterator = iter(iterable)

    while True:
        try:
            #пытаемся получить следующий элемент
            item = next(iterator)
            #выполняем действия с элементом (аналог тела цикла for)
            print(item)  # Здесь может быть любая логика
        except StopIteration:
            #ловим исключение "конца итерации"
            print("Конец итерации")
            break
#тестируем на разных типах данных
numbers = [1, 2, 3, 4, 5]
print("Список чисел:")
emulate_for(numbers)

print("\nСтрока:")
emulate_for("Hello")

print("\nКортеж:")
emulate_for((10, 20, 30))

print("\nДиапазон:")
emulate_for(range(3))