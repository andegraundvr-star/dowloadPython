#Координаты точки
class Point:
    __total_point = 0
    def __init__(self, x=0, y=0):
        self.__coordinat_x = x
        self.__coordinat_y = y
        Point.__total_point += 1
        self.nomber = self.get_point()
    def magic_str(self):
        return str(self.get_coordinat_x()), str(self.get_coordinat_y())
    def info_point(self):
        while True:
            try:
                coordinats = input('\nВведите новые координаты точки #{} через пробел (x y): '.format(self.nomber))
                x, y = map(float, coordinats.split())
                #используем сеттеры вместо прямого доступа к приватным атрибутам
                self.set_coordinat_x(x)
                self.set_coordinat_y(y)
                coord_x_str, coord_y_str = self.magic_str()
                print("Представлена точка #{} с координатами ( {}, {} )".format(self.nomber,coord_x_str,coord_y_str))
                break
            except ValueError:
                print("Ошибка: введите два числа через пробел!")
    #добавляем геттеры для счетчика и для каждой координаты
    def get_point(self):
        return Point.__total_point
    def get_coordinat_x(self):
        return self.__coordinat_x
    def get_coordinat_y(self):
        return self.__coordinat_y
    #сеттеры с валидацией
    def set_coordinat_x(self,x):
        if not isinstance(x, (int, float)):
            raise ValueError("Координата X должна быть числом")
        self.__coordinat_x = x
    def set_coordinat_y(self,y):
        if not isinstance(y, (int, float)):
            raise ValueError("Координата Y должна быть числом")
        self.__coordinat_y = y

#создаем экземпляр класса
this_point = Point()
this_point.info_point()
#создаем второй экземпляр класса
this_point_2 = Point()
this_point_2.info_point()

#использование геттеров для получения координат
print("\nКоординаты первой точки:")
print("X =", this_point.get_coordinat_x())
print("Y =", this_point.get_coordinat_y())

print("\nКоординаты второй точки:")
print("X =", this_point_2.get_coordinat_x())
print("Y =", this_point_2.get_coordinat_y())
#работа сеттеров
print("\n" + "="*50)
#изменяем координаты первой точки через сеттеры
print("\nИзменяем координаты первой точки:")
this_point.set_coordinat_x(100)
this_point.set_coordinat_y(200)
print("Новые координаты первой точки: X =", this_point.get_coordinat_x(), "Y =", this_point.get_coordinat_y())

#изменяем координаты второй точки через сеттеры
print("\nИзменяем координаты второй точки:")
this_point_2.set_coordinat_x(-50)
this_point_2.set_coordinat_y(75.5)
print("Новые координаты второй точки: X =", this_point_2.get_coordinat_x(), "Y =", this_point_2.get_coordinat_y())

# тестируем валидацию
print("\n" + "="*50)
print("Тестирование валидации:")
print("="*50)

try:
    this_point.set_coordinat_x("не число")  # Вызовет ошибку
except ValueError as e:
    print(f"Ошибка при установке X: {e}")

try:
    this_point.set_coordinat_y("не число")  # Вызовет ошибку
except ValueError as e:
    print(f"Ошибка при установке Y: {e}")
# Проверяем, что значения не изменились после ошибок
print("Координаты после попытки неверного ввода: X =", this_point.get_coordinat_x(), "Y =", this_point.get_coordinat_y())
