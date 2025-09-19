#битва
import random


#создаем класс Воин
class Warrior:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.actions = ['Блок', 'Удар', 'none']
    #созадем функцию выбора действия: удар или блок
    def choice_action(self):
        self.current_action = random.choice(self.actions)
        print("\n{} принял действие: {} ".format(self.name,self.current_action))
        return self.current_action
    #создаем функцию получения или не получения урона
    def take_damage(self, attacker_action):
        if attacker_action == 'Удар':
            if self.current_action == 'Блок':
                print("\n Воин {} блокировал удар".format(self.name))
                return False
            else:
                self.hp -= 20
                print("\n Воин {} получает damage 20, осталось {} здоровья".format(self.name, self.hp))
                return True
        return False
    #создаем функцию окончания поединка, когда кончается уровень очков здоровья и сообщение о поражении
    def is_defeated(self):
        if self.hp <= 0:
            return True
        return False
#создаем два класса участников битвы
class SubZero(Warrior):
    def __init__(self):
        super().__init__("Sub-Zero")
class LiuKang(Warrior):
    def __init__(self):
        super().__init__("Liu Kang")
#создаем функцию поединка
def battle():
    print("=== MORTAL KOMBAT ===")
    print("        FIGHT!")
    sub_zero = SubZero()
    liu_kang = LiuKang()
    round_num = 1
    while True:
        print("\n---------ROUND {}----------".format(round_num))
        #выбор действий
        sub_zero_action = sub_zero.choice_action()
        liu_kang_action = liu_kang.choice_action()
        #определение, кто атакует первым (случайный выбор)
        if random.choice([True, False]):
            #Sub-Zero атакует первым
            if sub_zero_action == 'Удар':
                liu_kang.take_damage(sub_zero_action)

            # Liu Kang атакует вторым, если не побежден
            if not liu_kang.is_defeated() and liu_kang_action == 'Удар':
                sub_zero.take_damage(liu_kang_action)
        else:
            #Liu Kang атакует первым
            if liu_kang_action == 'Удар':
                sub_zero.take_damage(liu_kang_action)

            # Sub-Zero атакует вторым, если не побежден
            if not sub_zero.is_defeated() and sub_zero_action == 'Удар':
                liu_kang.take_damage(sub_zero_action)
        #проверка условий победы
        if sub_zero.is_defeated():
            print("\nLiu Kang побеждает! FLAWLESS VICTORY!")
            print("\nВоин Sub-Zero повержен! Shang Tsung took his soul!")
            break
        if liu_kang.is_defeated():
            print("\nSub-Zero побеждает! FLAWLESS VICTORY!")
            print("\nВоин Liu Kang повержен! Shang Tsung took his soul!")
            break

        round_num += 1

#запуск битвы
battle()




