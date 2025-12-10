#  Координаты точки
class Point:
    total_point = 0  #классовый атрибут для подсчета всех точек
    def __init__(self, x=0, y=0):
        self.coordinat_x = x
        self.coordinat_y = y
        Point.total_point += 1  #увеличиваем счетчик при создании
        self.point_nomber = Point.total_point #уникальный номер точки
        print("\nСоздана точка #{} с координатами ({}, {})".format(self.point_nomber, self.coordinat_x, self.coordinat_y))
    #создаем функцию добавления координат точки
    def set_point(self):
        while True:
            try:
                coordinats = input('\nВведите новые координаты точки #{} через пробел (x y): '.format(self.point_nomber))
                x, y = map(float, coordinats.split())
                print("Заданы координаты ({}, {}) для точки {}".format(self.coordinat_x, self.coordinat_y, self.point_nomber))
                break
            except ValueError:
                print("Ошибка: введите два числа через пробел!")
#создаем экземпляр класса
this_point = Point()
this_point.set_point()
#создаем второй экземпляр класса
this_point_2 = Point()
this_point_2.set_point()
