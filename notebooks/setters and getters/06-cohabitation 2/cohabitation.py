#Совместное проживание — 2
import random

class Man:
    total_day = 0  # счетчик дней
    total_man = 0  # счетчик людей
    fur_coat_count = 0  # счетчик шуб
    total_food = 0 #счетчик еды
    cat_food_requested = False  #кто-то уже запросил покупку кошачьей еды


    def __init__(self, name, bank, refrigerator, catsfoods, entropy):
        Man.total_man += 1
        self.name = name
        self.hunger = 30 #будет переопределено
        self.happy = 100 #будет переопределено
        self.actions = ['играть', 'в магазин', 'на работу', 'поесть', 'гладить кота', 'убраться', 'за шубой', 'в магазин за кошачьей едой']
        self.bank = bank  #передаем экземпляр банка
        self.refrigerator = refrigerator  #передаем экземпляр холодильника
        self.catsfoods = catsfoods #передаем экземпляр склада кошачьей еды
        self.entropy = entropy #передаем экземпляр грязи
        self.current_action = None  #текущее действие

    def action_man(self):
        if self.hunger <= 0:
            print(f"{self.name} умер от голода RIP")
            return False
        elif self.happy <= 0:
            print(f"{self.name} умер от депрессии RIP")
            return False

        #создаем условия проверки всех ресурсов семьи перед выбором действия
        action_performed = False

        if self.hunger < 20:
            self.eat()
            action_performed = True
        elif self.bank.get_money() <= 100: #увеличиваем необходимый порог денег, чтобы было больше шуб и жена стала счатсливой
            self.work()
            action_performed = True
        elif self.refrigerator.get_reserve() <= 95: #в зависимости от количества членов семьи
            self.go_shopping()
            action_performed = True
        elif self.catsfoods.get_foods() <= 25: #в зависимости от количества котов делаем нижний порог пополнения кошачей еды
            self.go_shopping_for_cats()
            action_performed = True
        elif self.entropy.get_units() >= 90:
            self.do_it_cleaning()
            action_performed = True

        #случайное действие выбирается, если приорететных действий нет
        if not action_performed:
            self.random_action()
        #уменьшаем сытость только если человек не ел
        if self.current_action != 'поесть':
            self.hunger -= 10
        #уменьшаем счастье каждый день
        self.happy -= 5
        #увеличиваем грязь только если человек не убирался
        if self.current_action != 'убраться':
            self.entropy.increase_units(5)

        return True

    def eat(self):
        self.current_action = 'поесть'
        if self.refrigerator.get_reserve() >= 30:
            print(f"{self.name} поел из холодильника")
            self.refrigerator.decrease_reserve(30)
            Man.total_food += 30 #сохраняем значение съеденой еды в базу данных
            self.hunger = 30
        else:
            print(f"{self.name} хочет есть, но в холодильнике пусто!")
            self.go_shopping()

    def petting_a_cat(self):
        self.current_action = 'гладить кота'
        print(f"{self.name} решил погладить кота")
        self.happy += 5

    def do_it_cleaning(self):
        self.current_action = 'убраться'
        print(f"{self.name} начал делать уборку")
        self.entropy.decrease_units(100)

    def work(self):
        self.current_action = 'на работу'
        print(f"{self.name} пошел на работу")
        self.bank.increase_money(150)

    def go_shopping(self):
        self.current_action = 'в магазин'
        if self.bank.get_money() >= 30:
            print(f"{self.name} пошел в магазин")
            self.refrigerator.increase_reserve(30 * Man.total_man * 2) # за 1 поход покупаем двойной запас еды помноженное на количество человек
            self.bank.decrease_money(30 * Man.total_man)
        else:
            print(f"{self.name} хочет в магазин, но нет денег!")
            self.work()

    def go_shopping_for_cats(self):
        #дополнительная проверка на случай, если несколько человек успели вызвать метод
        if self.catsfoods.get_foods() > 40:  # Если уже купили достаточно
            print(f"{self.name}: кошачья еда уже куплена!")
            return
        self.current_action = 'в магазин'
        if self.bank.get_money() >= 30:
            print(f"{self.name} пошел в магазин за кошачьей едой")
            self.catsfoods.increase_foods(60) # за 1 поход пополняем сразу весь склад на двух котов
            self.bank.decrease_money(20)
            print(f"Кошачья еда пополнена! Теперь: {self.catsfoods.get_foods()}")
        else:
            print(f"{self.name} хочет в магазин, но нет денег!")
            self.work()

    def buy_fur_coat(self):
        self.current_action = 'за шубой'
        if self.bank.get_money() >= 350:
            print(f"{self.name} пошла за шубой")
            self.bank.decrease_money(350) #шубы стоят по 350
            Man.fur_coat_count += 1  #увеличиваем счетчик шуб
            self.happy += 60
            return True
        else:
            print(f"{self.name} хочет в магазин, но нет денег!")
            self.work()
            return False

    def random_action(self):
        self.current_action = random.choice(self.actions)
        print(f"{self.name} решил {self.current_action}")
        if self.current_action == 'играть':
            self.happy += 20
        elif self.current_action == 'в магазин за кошачьей едой':
            self.go_shopping_for_cats()
Man.cat_food_requested = False  #сбрасываем флаг для следующего дня
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

class Catsfoods:
    def __init__(self, foods=30):
        self.__foods = foods  #защищенный атрибут

    def get_foods(self):
        return self.__foods

    def increase_foods(self, amount):
        self.__foods += amount

    def decrease_foods(self, amount):
        if self.__foods >= amount:
            self.__foods -= amount
        else:
            self.__foods = 0

class Entropy:
    def __init__(self, units=0):
        self.__units = units  #защищенный атрибут

    def get_units(self):
        return self.__units

    def increase_units(self, amount):
        self.__units += amount

    def decrease_units(self, amount):
        if self.__units >= amount:
            self.__units -= amount
        else:
            self.__units = 0

#создаем новый класс мужа, наследуем от Man
class Husband(Man):
    #переопределяем метод __init__ для мужа
    def __init__(self, name, bank, refrigerator, catsfoods, entropy):
        super().__init__(name, bank, refrigerator, catsfoods, entropy)
        self.actions = ['играть', 'на работу', 'поесть', 'гладить кота','в магазин за кошачьей едой']
        self.hunger = 30
        self.happy = 100
    def work(self):  #переопределяем метод work
            self.current_action = 'на работу'
            print(f"{self.name} пошел на работу")
            self.bank.increase_money(150)
            self.happy += 5  #мужу нравится работать, а то может умереть
    def action_man(self):  #переопределяем метод для приорететный метод для мужа,а то у него проблемы с сичным счастьем
        #создаем условие проверки счастья перед выбором действия (приоретет)
        action_performed = False
        if self.happy < 15:
            self.current_action = 'на работу'
            print(f"{self.name} пошел на работу")
            self.work()  #вызываем метод work
            return True

        #вызываем родительский метод для основной логики
        return super().action_man()
#создаем новый класс жены, наследуем от Man
class Wife(Man):
    #переопределяем метод __init__ для жены
    def __init__(self, name, bank, refrigerator, catsfoods, entropy):
        super().__init__(name, bank, refrigerator, catsfoods, entropy)
        self.actions = ['в магазин', 'убраться', 'поесть', 'гладить кота','в магазин за кошачьей едой']
        self.hunger = 30
        self.happy = 100
    def go_shopping(self):  #переопределяем метод go_shopping
        self.current_action = 'в магазин'
        if self.bank.get_money() >= 30:
            print(f"{self.name} пошла в магазин")
            self.refrigerator.increase_reserve(10 * Man.total_man)
            self.bank.decrease_money(10 * Man.total_man)
            self.happy += 5  #жене нравится ходить по магазинам, чтобы не умерла (также, как играть для всех)
        else:
            print(f"{self.name} хочет в магазин, но нет денег!")

    def buy_fur_coat(self):  #метод только для жены
        self.current_action = 'за шубой'
        if self.bank.get_money() >= 350:
            print(f"{self.name} пошла за шубой")
            self.bank.decrease_money(350)
            Man.fur_coat_count += 1
            self.happy += 60
            return True
        else:
            print(f"{self.name} хочет шубу, но нет денег!")
            return False
    def action_man(self):  #переопределяем метод для жены .а то у нее проблемы с сичным счастьем
        #создаем условие проверки счастья перед выбором действия (приоретет)
        action_performed = False
        if self.happy < 15:
            print(f"{self.name} слишком несчастна без новой шубы в последнее время")
            self.buy_fur_coat()  #вызываем метод buy_fur_coat
            return True  #возвращаем True и не идем дальше

        #вызываем родительский метод для основной логики
        return super().action_man()

#создаем новый класс ребенка, наследуем от Man
class Children(Man):
    #переопределяем метод __init__ для ребенка
    def __init__(self, name, bank, refrigerator, catsfoods, entropy):
        super().__init__(name, bank, refrigerator, catsfoods, entropy)
        self.actions = ['играть', 'поесть', 'гладить кота','в магазин за кошачьей едой']
        self.hunger = 30
        self.happy = 100
    def work(self):  #переопределяем метод работы для ребенка
        print(f"{self.name} не может работать - он еще ребенок!")
        self.random_action()

    def go_shopping(self):  #переопределяем метод похода в магазин для ребенка
        print(f"{self.name} не может ходить в магазин один!")
        self.random_action()
    def action_man(self):  #переопределяем метод для ребенка, чтобы у него было чем пополнять уровень счастья
        #создаем условие проверки счастья перед выбором действия (приоретет)
        action_performed = False
        if self.happy < 15:
            self.current_action = 'играть'
            self.happy += 5
            print(f"{self.name} решил поиграть")
            return True

        #вызываем родительский метод для основной логики
        return super().action_man()

#создаем новый класс кота
class Cat:
    total_cats = 0 #счетчик котов
    #переопределяем метод __init__ для кота
    def __init__(self, name, catsfoods, entropy):
        self.name = name
        self.entropy = entropy #передаем экземпляр грязи
        self.catsfoods = catsfoods# передаем экземплчр екошачьец еды
        self.actions = ['драть обои', 'спать', 'поесть']
        self.hunger = 30 #у кота начальный уровень голода по условию 30
        Cat.total_cats += 1
    def eat(self):
        if self.catsfoods.get_foods() >= 10:
            self.catsfoods.decrease_foods(10)
            self.hunger += 20 #у кота степень сытости 2 к 1
            self.current_action = 'поесть'
        else:
            print(f"{self.name} хочет есть, но в запасах кошачьей еды пусто!")

    def pulls_claws(self):
        #print(f"{self.name} решил поточить когти об обои")
        self.entropy.increase_units(5)
    def action_man(self):  #переопределяем метод для кота
        if self.hunger <= 0:
            print(f"{self.name} умер от голода RIP")
            return False
        #создаем условие проверки голода перед выбором действия (приоретет)
        action_performed = False
        if self.hunger < 15:
            self.eat()
            action_performed = True
            print(f"{self.name} поел из запасов кошачей еды")
        #если кот не делал приорететное действие, то выбираем рандомное
        if not action_performed:
            action = random.choice(self.actions)
            self.current_action = action
            print(f"{self.name} решил {action}")
            if action == 'поесть':
                self.eat()
                #print(f"{self.name} поел из запасов кошачей еды")
            elif action == 'драть обои':
                self.pulls_claws()
        #уменьшаем сытость только если кот не ел
        if self.current_action != 'поесть':
            self.hunger -= 10

        return True

#создаем экземпляры банка, холодильника, склада кошачьей еды, уровня грязи
bank = Bank()
refrigerator = Refrigerator()
catsfoods = Catsfoods()
entropy = Entropy()


#создаем экземпляры людей и передаем им зависимости
man1 = Husband('Bob', bank, refrigerator,catsfoods, entropy)
man2 = Wife('Maria', bank, refrigerator, catsfoods, entropy)
man3 = Children('Cristofer', bank, refrigerator, catsfoods, entropy)
cat1 = Cat('Tigra', catsfoods, entropy)
cat2 = Cat('Suslic', catsfoods, entropy)
#заставляем людей жить
for i in range(1, 365):
    Man.total_day = i
    Man.cat_food_requested = False  #сбрасываем флаг вначале дня
    print(f"\n-= День {i} =-")
    if not man1.action_man():
        break
    if not man2.action_man():
        break
    if not man3.action_man():
        break
    if not cat1.action_man():
        break
    if not cat2.action_man():
        break

    #вывод состояния ресурсов через геттеры
    print(f"\nРесурсы: Съедено еды - {Man.total_food}, Деньги - {bank.get_money()}, Шубы - {Man.fur_coat_count}")
