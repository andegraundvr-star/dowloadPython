
#Окружность
import math
import random

class Cricle:
    total_point = 0  #классовый атрибут для подсчета всех центров окружностей
    #инициируем точки центров окружностей
    def __init__(self,x=0,y=0,r=1):
        self.coordinat_x = x
        self.coordinat_y = y
        self.radius = r
        Cricle.total_point += 1  #увеличиваем счетчик при создании
        self.point_nomber = Cricle.total_point #уникальный номер центра окружности
        print("\nСоздана окружность #{} с координатами центра ({}, {})".format(self.point_nomber, self.coordinat_x, self.coordinat_y))
    #добавляем возможности окружностей
    def action(self):
        K = random.randint(2, 5)
        ansver = random.choice(['yes', 'no'])
        try:
            if ansver == 'yes':
                self.new_radius = self.radius * K #увеличиваем радиус на рандомную велчину
                print("Для окружности #{} задан новый радиус, равный {}".format(self.point_nomber, K))
                self.perimeter = 2 * math.pi * self.new_radius
                self.S = math.pi * self.new_radius ** 2
                print(f"\nДля окружности № {self.point_nomber} инзменены характеристики: периметр = {self.perimeter:.2f}, площадь = {self.S:.2f}, new_radius = {self.new_radius}")
            elif ansver == 'no':
                self.new_radius = self.radius #не увеличиваем радиус на рандомную велчину
                print("Для окружности #{} радиус не изменился".format(self.point_nomber))
                self.perimeter = 2 * math.pi * self.new_radius
                self.S = math.pi * self.new_radius ** 2
                print(f"\nДля окружности № {self.point_nomber} заданы характеристики по умолчанию: периметр = {self.perimeter:.2f}, площадь = {self.S:.2f}, new_radius = {self.new_radius}")
        except ValueError:
            print("Ошибка: введите yes или no!")
    #создаем функцию определения пересечения с другой окружностью
    def crash(self,other):
        #вычисляем кратчайшее расстояние между центрами и сравниваем с суммой их радиутов
        distance = math.sqrt((self.coordinat_x - other.coordinat_x) ** 2 + (self.coordinat_y - other.coordinat_y) ** 2)
        summ_rad = self.radius + other.radius
        if distance < summ_rad:
            print("\nОкружности №{} и №{} пересекаются".format(self.point_nomber,other.point_nomber))
        elif distance == summ_rad:
            print("\nОкружности №{} и №{} касаются".format(self.point_nomber,other.point_nomber))
        else:
            print("\nОкружности №{} и №{} не пересекаются".format(self.point_nomber,other.point_nomber))
    #создаем функцию добавления координат точки центра окружности
    def set_point(self):
        while True:
            try:
                x = random.randint(0, 5)
                y = random.randint(0, 5)
                coordinats = [x, y]
                x, y = map(float,coordinats)
                self.coordinat_x, self.coordinat_y = x, y  #обновляем координаты
                print("\nЗаданы координаты ({}, {}) новой точки центра окружности № {} ".format(self.coordinat_x, self.coordinat_y, self.point_nomber))
                break
            except ValueError:
                print("Ошибка: введите два числа через пробел!")
#создаем экземпляр класса
this_point = Cricle()
this_point.set_point()
#увеличиваем первый объем
this_point.action()

#создаем второй экземпляр класса
this_point_2 = Cricle()
this_point_2.set_point()
#увеличиваем второй объем
this_point_2.action()
#проверяем пересечение
this_point.crash(this_point_2)

#создаем третий экземпляр класса
this_point_3 = Cricle()
this_point_3.set_point()
#увеличиваем второй объем
this_point_3.action()
#проверяем пересечение
this_point.crash(this_point_3)
this_point_2.crash(this_point_3)
this_point.crash(this_point_2)
