#Совместное проживание
import random

class Man:
    total_day = 0  # счетчик дней
    total_man = 0  # счетчик людей

    def __init__(self, name, bank, refrigerator):
        Man.total_man += 1
        self.name = name
        self.hunger = 50
        self.actions = ['играть', 'в магазин', 'на работу', 'поесть']
        self.bank = bank  #передаем экземпляр банка
        self.refrigerator = refrigerator  #передаем экземпляр холодильника

    def action_man(self):
        if self.hunger <= 0:
            print(f"{self.name} умер от голода RIP")
            return False

        if self.hunger < 20:
            self.eat()
        elif self.bank.get_money() <= 50:
            self.work()
        elif self.refrigerator.get_reserve() <= 10:
            self.go_shopping()
        else:
            self.random_action()

        if self.actions != self.actions[3]:#уменьшаем сытость только если человек не ел
            self.hunger -= 10

        return True

    def eat(self):
        if self.refrigerator.get_reserve() >= 20:
            print(f"{self.name} поел из холодильника")
            self.refrigerator.decrease_reserve(20)
            self.hunger = 50
        else:
            print(f"{self.name} хочет есть, но в холодильнике пусто!")
            self.go_shopping()

    def work(self):
        print(f"{self.name} пошел на работу")
        self.bank.increase_money(50)

    def go_shopping(self):
        if self.bank.get_money() >= 30:
            print(f"{self.name} пошел в магазин")
            self.refrigerator.increase_reserve(40)
            self.bank.decrease_money(30)
        else:
            print(f"{self.name} хочет в магазин, но нет денег!")
            self.work()

    def random_action(self):
        self.current_action = random.choice(self.actions)
        print(f"{self.name} решил {self.current_action}")

class Refrigerator:
    def __init__(self, reserve=50):
        self.__reserve = reserve  #защищенный атрибут

    def get_reserve(self):
        return self.__reserve

    def increase_reserve(self, amount):
        self.__reserve += amount

    def decrease_reserve(self, amount):
        if self.__reserve >= amount:
            self.__reserve -= amount
        else:
            self.__reserve = 0

class Bank:
    def __init__(self, money=100):
        self.__money = money  #защищенный атрибут

    def get_money(self):
        return self.__money

    def increase_money(self, amount):
        self.__money += amount

    def decrease_money(self, amount):
        if self.__money >= amount:
            self.__money -= amount
        else:
            self.__money = 0

#создаем экземпляры банка и холодильника
bank = Bank()
refrigerator = Refrigerator()

#создаем экземпляры людей и передаем им зависимости
man1 = Man('Bob', bank, refrigerator)
man2 = Man('Maria', bank, refrigerator)

#заставляем людей жить
for i in range(1, 365):
    Man.total_day = i
    print(f"\n-= День {i} =-")
    if not man1.action_man():
        break
    if not man2.action_man():
        break

    #вывод состояния ресурсов через геттеры
    print(f"\nРесурсы: Еда - {refrigerator.get_reserve()}, Деньги - {bank.get_money()}")
