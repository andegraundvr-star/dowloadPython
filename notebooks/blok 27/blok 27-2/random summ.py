#случайная сумма
import random

class Rand_iter:
    def __init__(self, count):
        self.count = count #задаем на входе толко количество элементов
        print(f"\nНовое количество элементов {self.count}")
    def __iter__(self):
        self.current = 0 #текущее значение
        self.index = 0 #текущий индекс
        return self
    def __next__(self):
        #задаем условие для стопа итерации
        if self.index > self.count:
            raise StopIteration
        #генерируем случайное число от 0 до 1
        random_num = random.randint(0, 100) / 100.0
        #прибавляем предыдущее значение (не сумму!)
        self.current += random_num
        self.index += 1
        return round(self.current, 2)

#использование - создаем экземпляр, на воходе количество индексов в списке
iterator = Rand_iter(4)
#вызываем метод класса
random_list = list(iterator)
print(random_list)
#вызываем метод класса еще раз с другим количеством элементов
iterator2 = Rand_iter(8)
random_list2 = list(iterator2) #на вход подаем второй экземпляр объекта iterator2
print(random_list2)