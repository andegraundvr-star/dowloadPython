#А-а-автомобиль!
import random
import  math
#создаем родительский класс с общими атрибутами
class Vehicle:
    total_vehicle = 0  #классовый атрибут для подсчета всех ТС в области
    #инициируем начальное положение и вектор направления движения ТС
    def __init__(self, name, x, y, r):
        Vehicle.total_vehicle += 1
        self.name = name
        self.coordinat_x = float(x)
        self.coordinat_y = float(y)
        #начальный радиус относительно нуля
        self.radius_relative_to_zero = float(r)
        self.vehicle_nomber = Vehicle.total_vehicle #уникальный номер ТС
        print("\nОбнаружено транспортное средство #{} в точке на карте с координатами  ({}, {})".format(self.vehicle_nomber, self.coordinat_x, self.coordinat_y))

    #создаем метод пройденного расстояния ТС
    def get_distance(self):
       return random.randint(1, 5) #произвольное расстояние
    #основной метод движения, который должен переопределяется в дочерних классах
    def move(self):
        #получаем пройденное расстояние вызываем методом distance()
        distance = self.get_distance()
        #задаем случайный угол поворота в одну или в другую сторону
        right_or_left = random.choice([1, -1])
        #ограничиваем возможность единовременного поворота ТС до прямого угла
        angle_change = right_or_left * random.randint(0, 90)
        #прибавляем угол повотора к начальному радиусу
        new_angle = self.radius_relative_to_zero + angle_change
        #преобразуем градусы в радианы
        angle_radians = math.radians(new_angle)
        #вычисляем новые координаты
        x_new = self.coordinat_x + distance * math.sin(angle_radians)
        y_new = self.coordinat_y + distance * math.cos(angle_radians)
        self.coordinat_x, self.coordinat_y = x_new, y_new
        self.radius_relative_to_zero = new_angle
        print(f"Транспортное сроедство '{self.name}' повернуло на {angle_change}°, проехало {distance} км. Новые координаты: ({x_new:.2f}, {y_new:.2f})")

        return distance

#создаем новый класс, наследуем от Vehicle
class Car(Vehicle):
    #переопределяем метод move для автомобиля
    def move(self):
        distance = super().move()
        print(f"Автомобиль {self.name} завершил движение")
        return distance

#создаем новый класс, вводим новые атрибуты
class Bus(Vehicle):
    def __init__(self, name, x, y, r):
        super().__init__(name, x, y, r)
        #вводим новые поля с числом пассажиров и деньгами в кассе
        self.number_of_passengers = random.randint(0, 22)
        self.payment_per_km = 3.1  #плата за км
        self.total_money = 0
    #создаем метод изменения пассажиров и денег
    def update_passengers(self):
        change = random.randint(-5, 5)
        self.number_of_passengers = max(0, self.number_of_passengers + change)
        return change
    #переопределяем метод move для автобуса
    def move(self):
        distance = super().move()
        #обновляем пассажиров и деньги
        passenger_change = self.update_passengers()
        money_earned = distance * self.number_of_passengers * self.payment_per_km
        self.total_money += money_earned
        if passenger_change > 0:
            print(f"На остановке зашло {passenger_change} пассажиров")
        elif passenger_change < 0:
            print(f"На остановке вышло {abs(passenger_change)} пассажиров")

        print(f"Текущее количество пассажиров: {self.number_of_passengers}")
        print(f"Заработано за поездку: {money_earned:.2f} руб.")
        print(f"Общая сумма в кассе: {self.total_money:.2f} руб.")

        return distance
#создаем экземпляры классов
this_car = Car(name='Жигуленок', x=1, y=2, r=45)
this_bus = Bus(name='Пазик', x=3, y=5, r=0)

#вызываем один метод move() для каждого транспортного средства
print("\n-= Движение автомобиля =-")
this_car.move()
print("\n-= Еще одно движение автомобиля =-")
this_car.move()

print("\n-= Движение автобуса =-")
this_bus.move()

print("\n-= Еще одно движение автобуса =-")
this_bus.move()
print("\n-= Еще одно движение автобуса =-")
this_bus.move()
print("\n-= Еще одно движение автобуса =-")
this_bus.move()