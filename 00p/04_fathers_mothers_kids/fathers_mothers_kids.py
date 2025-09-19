#Отцы, матери и дети
#from datetime import datetime
import random


class Children:
    def __init__(self, name,father_age):

        self.name = name
        #задаем возраст ребенка от входного параметра возраста отца
        self.old =  random.randint(1, father_age - 16)
        self.condition = ['Спокойствие', 'Тревога']
        self.hunger = ['голод', 'сытость']
        self.current_condition = None
        self.current_hunger = None
    #создаем функцию выбора параметров ребенка
    def choice_parametrs(self):
        #now = datetime.now()
        #hours = now.hour
        self.current_condition = random.choice(self.condition)
        self.current_hunger = random.choice(self.hunger)
        print("\n У {} , {} лет сейчас состояние: {} и {} ".format(self.name, self.old, self.current_condition, self.current_hunger))
        return self.current_condition, self.current_hunger

class Father:
    def __init__(self,name):
        self.name = name
        self.old = random.randint(17,60)
        self.children = []
    #добавялем детей
    def add_child(self, child_name):
        self.children.append(Children(child_name, self.old))
    #инициализация действий отца
    def info(self):
        print("\nМеня зовут {}, мне {} лет, у меня {} детей".format(self.name, self.old, len(self.children)))
        for child in self.children:
            condition, hunger = child.choice_parametrs()
            if condition == 'Тревога':
                print(f"\nРебенок {child.name} тревожится, батя успокоил малыша")
                child.current_action = 'Спокойствие'
            if hunger == 'голод':
                print(f"\nРебенок {child.name} голоден, батя накормил ребенка")
                child.current_action = 'сытость'

#запускаем параметры отца и функцию действий отца
father = Father("Иван")
father.add_child("Маша")
father.add_child("Петя")

father.info()
