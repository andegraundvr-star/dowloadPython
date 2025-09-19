#Машина 2
#создаем класс
class Toyota:
    color_car = 'red'
    price = 1000000
    speed_max = 200
    total_cars = 0
    speed_now = 0
    #создаем функцию изменения количества вызова автомобилей и текущей скорости
    def __init__(self):
        Toyota.total_cars += 1
        self.car_number = Toyota.total_cars
        self.speed_now = 0
    #создаем функцию текущей скорости автомобиля
    def set_speed(self):
        while True:
            try:
                speed = int(input('Введите текущую скорость автомобиля #{}: '.format(self.car_number)))
                if 0 <= speed <= self.speed_max:
                    self.speed_now = speed
                    break
                else:
                    print(f"Скорость должна быть от 0 до {self.speed_max} км/ч!")
            except ValueError:
                print("Ошибка: введите целое число!")

    #создаем функцию вывода информации о машине
    def info(self):
        print("машина: {}".format(self.car_number))
        print("Цвет: {}".format(self.color_car))
        print("Цена: {} руб.".format(self.price))
        print("Максимальная скорость: {} км/ч".format(self.speed_max))
        print("Текущая скорость: {} км/ч".format(self.speed_now))
#создаем экземпляр класса
my_car = Toyota()
my_car.info()
#создаем еще один экземпляр с другой заданной скоростью
my_car_2 = Toyota()
my_car_2.set_speed()
my_car_2.info()
#создаем еще один экземпляр с другой заданной скоростью
my_car_3 = Toyota()
my_car_3.set_speed()
my_car_3.info()

