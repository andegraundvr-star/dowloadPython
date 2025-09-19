
#Семья
#создаем класс и атрибуты класса
class Famaly:
    name = 'Тутанхамон'
    gold = 1000000
    house = False
    salary = 0
    total_try = 0
    discont = 0
    #создаем функцию отображения информации
    def info(self):
        print("\nФамилия семьи {}: ".format(self.name))
        print("Cколько Голды {}: ".format(self.gold))
        print("Сколько заработали {}: ".format(self.salary))
        print(f"Есть ли дом : {'Да' if self.house else 'Нет'} ")
    #создаем функцию заработка денег
    def increase_money(self):
        while True:
            try:
                money = int(input("\nВведите сумму, заработанную семьей {} : ".format(self.name)))
                if money < 0:
                    print("Сумма не может быть отрицательной!")
                    continue
                self.salary = money
                self.gold += money
                print("Семья {} заработала {} золота!".format(self.name,money))
                break
            except ValueError:
                print("Ошибка: введите целое число!")
    #создаем функцию попытки покупки дома и применеия скидочной системы
    def buy(self):
        Famaly.total_try += 1
        base_price = 18000000
        if Famaly.total_try > 1:
            self.discont = 10
            house_price = base_price * (100 - self.discont) / 100
        else:
            house_price = base_price

        print("\nПопытка покупки дома семьей {}...".format(self.name))
        print("Текущее состояние: {} золота".format(self.gold))
        print("Стоимость дома: {} золота,скидка ({}%)".format(house_price, self.discont))
        if self.gold >= house_price:
            self.gold -= house_price
            self.house = True
            print("Поздравляем! Семья {} купила дом!".format(self.name))
            print("Остаток золота: {}".format(self.gold))
        else:
            needed = house_price - self.gold
            print("Not enough money! about {}. Необходимо еще {}".format(self.name, needed))

#создаем экземпляр класса
try_buy_house = Famaly()
try_buy_house.info()
#создаем еще один экземпляр с попыткой покупки дома
try_buy_house_2 = Famaly()
try_buy_house_2.increase_money()
try_buy_house_2.buy()
try_buy_house_2.info()

#создаем еще один экземпляр с попыткой покупки дома
try_buy_house_3 = Famaly()
try_buy_house_3.increase_money()
try_buy_house_3.buy()
try_buy_house_3.info()




