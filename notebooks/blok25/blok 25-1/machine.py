#Машина
import random

#создаем класс
class Toyota:
    color_car = 'red'
    price = 1000000
    speed_max = 200
    speed_now = 0
    #создаем функцию изменения скорости при создании экземпляра
    def __init__(self):
        self.speed_now = random.randint(0, self.speed_max)

    #создаем функцию вывода информации о машине
    def info(self):
        print(f"Цвет: {self.color_car}")
        print(f"Цена: {self.price} руб.")
        print(f"Максимальная скорость: {self.speed_max} км/ч")
        print(f"Текущая скорость: {self.speed_now} км/ч")
#создаем экземпляр класса
my_car = Toyota()

#выводим информацию о машине
my_car.info()

#создаем еще один экземпляр с другой случайной скоростью
my_car_2 = Toyota()
my_car_2.info()

#создаем еще один экземпляр с другой случайной скоростью
my_car_3 = Toyota()
my_car_3.info()

