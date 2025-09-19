#юниты
#создаем родительский класс
class Unit:
    def __init__(self,hp_lvl=100):
        self.__hp_lvl = hp_lvl
        self.__take_it_damage = 0
    #геттеры для доступа к приватным полям
    def get_hp_lvl(self):
        return self.__hp_lvl
    def get_take_it_damage(self):
        return self.__take_it_damage

    #сеттеры для изменения приватных полей
    def set_hp_lvl(self,hp):
        if hp < 0:
            self.__hp_lvl = 0  #ХП не может быть отрицательным
        else:
            self.__hp_lvl = hp
    def set_take_it_damage(self,damage):
        if damage < 0:
            self.__take_it_damage = 0  # урон не может быть отрицательным
        else:
            self.__take_it_damage = damage

    #базовый метод действия - получает урон
    def action(self):
        self.set_take_it_damage(0) #сбрасываем полученный урон
        return f"Получает урон: {self.get_take_it_damage()}, осталось ХП: {self.get_hp_lvl()}"
    def __str__(self):
        return f"Юнит: ХП={self.get_hp_lvl()}, полученный урон={self.get_take_it_damage()}"
#создаем дочерние классы
class Soldjer(Unit):
    #Переопределяем метод для солдата
    def action(self):
        damage = 20
        self.set_take_it_damage(damage) #устанавливаем дамаг
        new_hp = self.get_hp_lvl() - damage  #вычисляем новое ХП
        self.set_hp_lvl(new_hp)  #устанавливаем новое ХП
        return f"Солдат получает урон {self.get_take_it_damage()}, осталось ХП: {self.get_hp_lvl()}"

class Usualy_member(Unit):
    def action(self):
        damage = 2 * 20
        self.set_take_it_damage(damage) #устанавливаем дамаг
        new_hp = self.get_hp_lvl() - damage  #вычисляем новое ХП
        self.set_hp_lvl(new_hp)  #устанавливаем новое ХП
        return f"обычный человек получает урон {self.get_take_it_damage()}, осталось ХП: {self.get_hp_lvl()}"

this_object = Soldjer(hp_lvl=100)
two_object = Usualy_member(hp_lvl=100)
print("Начальное состояние:")
print(this_object)
print(two_object)
print()
#запускаем полиформизм несколько раз
print("Действия:")
print(this_object.action())
print(this_object.action())
print(two_object.action())
print(two_object.action())
print()

print("Конечное состояние:")
print(this_object)
print(two_object)


this_object.action()
this_object.action()
two_object.action()
two_object.action()
