#Человек
class Human:
    __total_humans = 0
    def __init__(self,name,old):
        self.__name = name
        self.__old = old
        Human.__total_humans +=1
        self.__nomber = Human.__total_humans
    def info(self):
        return self.get_humans(), self.get_name(), self.get_old()

    #добавляем геттеры
    def get_humans(self):
        return self.__nomber
    def get_name(self):
        return self.__name
    def get_old(self):
        return self.__old
    #добавляем сеттеры с валидацией
    def set_name(self,name):
        if not isinstance(name, str):
            raise ValueError("Имя не должно быть числом")
        self.__name = name
    def set_old(self,old):
        if not isinstance(old,int):
            raise ValueError("Возраст должен быть целым числом")
        if old < 1 or old > 100:
            raise ValueError("Возраст должен быть в диапазоне от 1 до 100")
        self.__old = old

#создаем экземпляр класса
this_man = Human('Маша', 25)
this_man.info()
#создаем второй экземпляр класса
second_man = Human('Наташа', 30)
second_man.info()
#использование геттеров для получения информации
print("информация о людях:")
print(f"{this_man.get_humans()} человек {this_man.get_name()}")
print(this_man.get_old())

print(f"{second_man.get_humans()} человек {second_man.get_name()}")
print(second_man.get_old())

#использование сеттеров для измененния информации и контроля ввода
print(f"\nИзменяем информацию о {this_man.get_humans()} человеке:")
this_man.set_name('Олег')
this_man.set_old(11)
print(f"{this_man.info()}")
print(f"\nИзменяем информацию о {second_man.get_humans()} человеке:")
second_man.set_name('привет')
second_man.set_old(50)
print(f"{second_man.info()}")
#тест валидации
try:
    second_man.set_old('лунатикам')  # Вызовет ошибку
except ValueError as e:
    print(f"Ошибка при вводе возраста: {e}")
try:
    second_man.set_old(150)  # Вызовет ошибку (выход за диапазон)
except ValueError as e:
    print(f"Ошибка при установке возраста: {e}")

try:
    second_man.set_name(123)  # Вызовет ошибку (число вместо строки)
except ValueError as e:
    print(f"Ошибка при установке имени: {e}")
#проверка после значений после не правльной валидации
print("\nПроверка после значений после не правльной валидации")
print("Информация по людям: имя - {}, возраст {}".format(second_man.get_humans(), second_man.get_name(), second_man.get_old()))
print(f"взять полное инфо {this_man.info()}, {second_man.info()}")
