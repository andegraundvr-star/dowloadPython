#роботы
import random
from datetime import datetime
class Robot:
    def __init__(self,model):
        self.model = model
        self.is_operating = False  # статус работы

    #метод только для родительского класса
    def operate(self):
        self.is_operating = True

class Vacuum_cleaner(Robot):
    def __init__(self,model):
        super().__init__(model)
        now = datetime.now()
        hours = now.hour
        full_tank = round(hours * 100 / 24, 2)
        print(f"Робот {self.model} пылесосит пол, занятость мешка: {full_tank} %")
class Warrior(Robot):
    def __init__(self,model,weapon):
        super().__init__(model)
        self.weapon = weapon
        print(f"Робот {self.model} проводит защиту военного объекта с помощью {self.weapon}")
class Submarine(Robot):
    def __init__(self,model):
        super().__init__(model)
        self.depth = random.randint(10,100)
        print(f"Робот {self.model} проводит защиту военного объекта на глубине: {self.depth} метров")

this_object = Robot('not_name')
this_object.operate()

two_object = Vacuum_cleaner('C3PO')
two_object.operate()

three_object = Warrior('cy-51','ракеты воздух-земля')
three_object.operate()

four_object = Submarine('american_pie')
four_object.operate()

