import random

#сначала определим классы эффектов
class Steam:
    def __init__(self):
        self.name = '-Steam-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Пар встречается с огнём - усиливается пар!")
            return self
        elif isinstance(other, Wind):
            print("Пар встречается с ветром - появляется шторм!")
            return Storm()
        else:
            print("Пар не взаимодействует с этим элементом")
            return self

class Lightning:
    def __init__(self):
        self.name = '-Lightning-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Молния встречается с водой - появляется пар и электрический разряд!")
            return Steam()
        else:
            print("Молния не взаимодействует с этим элементом")
            return self

class Lava:
    def __init__(self):
        self.name = '-Lava-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Лава встречается с водой - появляется камень и пар!")
            return Steam()
        else:
            print("Лава не взаимодействует с этим элементом")
            return self

class Storm:
    def __init__(self):
        self.name = '-Storm-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Earth):
            print("Шторм встречается с землей - появляется грязь!")
            return Mud()
        else:
            print("Шторм не взаимодействует с этим элементом")
            return self

class Mud:
    def __init__(self):
        self.name = '-Mud-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Грязь встречается с огнём - появляется кирпич!")
            return self
        else:
            print("Грязь не взаимодействует с этим элементом")
            return self

class Poison:
    def __init__(self):
        self.name = '-Poison-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Яд встречается с огнём - появляется токсичный пар!")
            return Steam()
        else:
            print("Яд не взаимодействует с этим элементом")
            return self

class Dust:
    def __init__(self):
        self.name = '-Dust-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Пыль встречается с водой - появляется грязь!")
            return Mud()
        else:
            print("Пыль не взаимодействует с этим элементом")
            return self

class Miasma:
    def __init__(self):
        self.name = '-Miasma-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Смрад встречается с огнём - очищается воздух!")
            return Wind()
        else:
            print("Смрад не взаимодействует с этим элементом")
            return self

class Abyss:
    def __init__(self):
        self.name = '-Abyss-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Бездна встречается с огнём - поглощает его!")
            return self
        else:
            print("Бездна не взаимодействует с этим элементом")
            return self

#потом определим основные классы элементов
class Fire:
    def __init__(self):
        self.name = '-Fire-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Огонь встречается с водой - появляется пар!")
            return Steam()
        elif isinstance(other, Wind):
            print("Огонь встречается с воздухом - появляется молния!")
            return Lightning()
        elif isinstance(other, Earth):
            print("Огонь встречается с землей - появляется лава!")
            return Lava()
        else:
            print("Огонь не взаимодействует с этим элементом")
            return self

class Water:
    def __init__(self):
        self.name = '-Water-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Fire):
            print("Вода встречается с огнём - появляется пар!")
            return Steam()
        elif isinstance(other, Wind):
            print("Вода встречается с воздухом - появляется шторм!")
            return Storm()
        elif isinstance(other, Earth):
            print("Вода встречается с землей - появляется грязь!")
            return Mud()
        elif isinstance(other, Dark):
            print("Вода встречается с тьмой - появляется яд!")
            return Poison()
        else:
            print("Вода не взаимодействует с этим элементом")
            return self

class Wind:
    def __init__(self):
        self.name = '-Wind-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Воздух встречается с водой - появляется шторм!")
            return Storm()
        elif isinstance(other, Fire):
            print("Воздух встречается с огнем - появляется молния!")
            return Lightning()
        elif isinstance(other, Earth):
            print("Воздух встречается с землей - появляется пыль!")
            return Dust()
        elif isinstance(other, Dark):
            print("Воздух встречается с тьмой - появляется смрад!")
            return Miasma()
        else:
            print("Воздух не взаимодействует с этим элементом")
            return self

class Earth:
    def __init__(self):
        self.name = '-Earth-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Земля встречается с водой - появляется грязь!")
            return Mud()
        elif isinstance(other, Fire):
            print("Земля встречается с огнем - появляется лава!")
            return Lava()
        elif isinstance(other, Wind):
            print("Земля встречается с воздухом - появляется пыль!")
            return Dust()
        elif isinstance(other, Dark):
            print("Земля встречается с тьмой - появляется бездна!")
            return Abyss()
        else:
            print("Земля не взаимодействует с этим элементом")
            return self

class Dark:
    def __init__(self):
        self.name = '-Dark-'

    def action(self):
        print(f"использован {self.name}")

    def __add__(self, other):
        if isinstance(other, Water):
            print("Тьма встречается с водой - появляется яд!")
            return Poison()
        elif isinstance(other, Earth):
            print("Тьма встречается с землей - появляется бездна!")
            return Abyss()
        elif isinstance(other, Wind):
            print("Тьма встречается с воздухом - появляется смрад!")
            return Miasma()
        else:
            print("Тьма не взаимодействует с этим элементом")
            return self

#создаем объекты
fire = Fire()
water = Water()
wind = Wind()
earth = Earth()
dark = Dark()

#выводим объекты
print("Базовые элементы:")
fire.action()
water.action()
wind.action()
earth.action()
dark.action()

#взаимодействий базовых классов
print("\n-= Взаимодействия базовых элементов =-")
result1 = fire + water
result1.action()

result2 = water + fire
result2.action()

result3 = earth + wind
result3.action()

result4 = wind + earth
result4.action()

result5 = fire + dark
result5.action()

result6 = dark + wind
result6.action()

result7 = wind + dark
result7.action()

#взаимодействия базовых классов с новыми
print("\n-= Взаимодействия с эффектами =-")
steam = fire + water
storm = steam + wind
storm.action()

mud = water + earth
mud.action()

lightning = fire + wind
poison = lightning + water
poison.action()

#создаем цепочку преобразований
print("\n-= Цепочка преобразований =-")
start = fire + water  #пар
next_step = start + wind  #шторм
final = next_step + earth  #грязь
final.action()
