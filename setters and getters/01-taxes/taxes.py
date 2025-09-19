#налоги

#класс для установки начальных денег
class InputMoney:
    #cтатический метод для установки начальных денег
    @staticmethod
    def set_initial_money():
        while True:
            try:
                money = float(input(f"Введите изначальное количество ваших денег: "))
                #self.money = money #устанавливаем деньги для каждого объекта
                Property.total_money = money  #устанавливаем общие деньги
                print(f"Установлен бюджет: {Property.total_money}")
                break
            except ValueError:
                print("Ошибка: введите число!")
#родительский класс
class Property:
    total_money = 0
    #методы для родительского класа
    def __init__(self, name):
        self.name = name
        self.worth = 0  #стоимость имущества

    #метод изменения стоимости имущества
    def set_worth(self):
        while True:
            try:
                worth = float(input(f"Веедите стоимоть {self.name} имущства: "))
                self.worth = worth
                break
            except ValueError:
                print("Ошибка: введите число!")
    #метод для оплаты налога
    def pay_tax(self):
        tax = self.calculate()
        if Property.total_money >= tax:
            Property.total_money -= tax
            return True
        else:
            print(f"Недостаточно денег для оплаты налога! Не хватает: {tax - Property.total_money:.2f}")
            return False
    def calculate(self):
        #базовая реализация будет переопределена
        return self.worth / 1000
    #метод вывода общей информации
    def info(self):
        tax = self.calculate()
        print(f"стоимость имущества {self.name} равно {self.worth:.2f}")
        print(f"налог на имущество {tax:.2f}")
        print(f"количество денег на счету {Property.total_money:.2f}")

#дочернике классы
class Apartment(Property):
    def calculate(self):#переопределяем метод
        return self.worth / 1000
class Car(Property):
    def calculate(self): #переопределяем метод
        return self.worth / 200
class CountryHouse(Property):
    def calculate(self):#переопределяем метод
        return self.worth / 500


#создаем экземпляры
this_object = Apartment(name = "квартира-дом")
two_object = Car(name = "Тойота")
three_object = CountryHouse(name = "Лесная сказка")
print("Установка начального бюджета:")
InputMoney.set_initial_money()  #используем классовый метод

#используем методы изменения стоимоти объекта и оплаты налога за объект
this_object.set_worth()
two_object.set_worth()
three_object.set_worth()

#запускаем полиформизм по каждому объекту
print("\nИнформация первого объекта:")
this_object.pay_tax()
this_object.info()
print("\nИнформация второго объекта:")
two_object.pay_tax()
two_object.info()
print("\nИнформация третьего объекта:")
three_object.pay_tax()
three_object.info()






