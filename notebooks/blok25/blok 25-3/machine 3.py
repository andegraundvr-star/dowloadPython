#машина 3
class Toyota:
    total_cars = 0  #классовый атрибут для подсчета всех автомобилей
    def __init__(self):
       self.color_car = 'red'
       self.price = 1000000
       self.speed_max = 200
       self.speed_now = 0
       Toyota.total_cars += 1  #увеличиваем счетчик при создании
       self.car_number = Toyota.total_cars  #уникальный номер автомобиля

       print("\nСоздана новая машина #{}:".format(self.car_number))
       print("Цвет: {}".format(self.color_car))
       print("Цена: {} руб.".format(self.price))
       print("Максимальная скорость: {} км/ч".format(self.speed_max))
       print("Текущая скорость: {} км/ч".format(self.speed_now))
    #создаем функцию текущей скорости автомобиля
    def set_speed(self):
       while True:
           try:
               speed = int(input('\nВведите текущую скорость автомобиля #{}: '.format(self.car_number)))
               if 0 <= speed <= self.speed_max:
                   self.speed_now = speed
                   print("Установлена скорость {} км/ч! для автомобиля №{}".format(speed, self.car_number))
                   break
               else:
                   print("Скорость должна быть от 0 до {} км/ч!".format(self.speed_max))
           except ValueError:
               print("Ошибка: введите целое число!")
#создаем экземпляр класса
this_car = Toyota()
#this_car.__init__()
this_car.set_speed()

