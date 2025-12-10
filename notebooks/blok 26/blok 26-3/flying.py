#полет
class Can_fly:

    def __init__(self,name, height = 0, speed = 0):
        self.__name = name
        self.__height = height
        self.__speed = speed

    #геттеры для доступа к приватным полям
    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_speed(self):
        return self.__speed

    #сеттеры для изменения приватных полей
    def set_height(self, height):
        self.__height = height
    def set_speed(self, speed):
        self.__speed = speed

    #создаем 4 метода для последующего переопределения
    def take_off(self):
        pass
    def fly(self):
        pass
    def land(self):
        self.set_height(0)  #сбрасываем скорость
        self.set_speed(0)   #сбрасываем высоту
        print(f"{self.get_name()} приземлилась, высота изменилась на: {self.get_height()}, а скорость стала {self.get_speed()}")
        return f"высота: {self.get_height()}, скорость: {self.get_speed()}"
    def display_statistics(self):
        print(f"-=текущие стистические данные=-: {self.__name} - высота: {self.get_height()}, скорость: {self.get_speed()}")
        return f"высота: {self.get_height()}, скорость: {self.get_speed()}"
class Battlefly(Can_fly):
    #Переопределяем методы для бабочки
    def take_off(self):
        self.set_height(1)    #используем сеттер родителя, меняем высоту
        self.set_speed(0.5)   #используем сеттер родителя, меняем скорость
        print(f"Для {self.get_name()} определена новая высота {self.get_height()} и скорость {self.get_speed()}")
    def fly(self):
        self.set_height(0.5)    #используем сеттер родителя, меняем высоту
        self.set_speed(1.5)   #используем сеттер родителя, меняем скорость
        print(f"В процессе полета {self.get_name()} высота изменилась на: {self.get_height()}, а скорость стала {self.get_speed()}")

class Rocket(Can_fly):
    #Переопределяем методы для ракеты
    def take_off(self):
        self.set_height(500)    #используем сеттер родителя, меняем высоту
        self.set_speed(10000)   #используем сеттер родителя, меняем скорость
        print(f"Для {self.get_name()} определена новая высота {self.get_height()} и скорость {self.get_speed()}")
    def fly(self):
        self.set_height(10000)    #используем сеттер родителя, меняем высоту
        self.set_speed(11000)   #используем сеттер родителя, меняем скорость
        print(f"В процессе полета {self.get_name()} высота изменилась на: {self.get_height()}, а скорость стала {self.get_speed()}")
    def boom(self):
        print(f"{self.get_name()} долетела до луны")

#создаем экземпляры
this_object = Battlefly(name = "Крапивница")
two_object = Rocket(name = "Союз")
print("Начальное состояние:")
this_object.display_statistics()  #выводим статистику
two_object.display_statistics()   #выводим статистику
print()


#запускаем полиформизм несколько раз
print("Действия первого объекта:")
this_object.take_off()
this_object.fly()
this_object.display_statistics()
this_object.land()

print("Действия второго объекта:")
two_object.take_off()
two_object.fly()
two_object.fly()  # еще раз летим
two_object.display_statistics()
two_object.boom()
two_object.land()
two_object.display_statistics()

print()

print("Конечное состояние:")
this_object.display_statistics()  #выводим статистику
two_object.display_statistics()   #выводим статистику





