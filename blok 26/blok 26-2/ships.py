#Корабли
class Ship:
    def __init__(self, model):
        self.model = model
        self.in_action = True
        self.action_text_active = "находится в пути"
        self.action_text_inactive = "стоит в порту"
        self.model_prefix = "Модель корабля"
    #Метод для изменения статуса действия
    def set_action_status(self, status):
        self.in_action = status
    def action(self):
        print(f" {self.model_prefix}: {self.model}")
        if self.in_action:
            print(f"корабль {self.model} {self.action_text_active}")
        else:
            print(f"корабль {self.model} {self.action_text_inactive}")
class Warrior_ship(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon
        self.action_text_active = "участвует в атаке"
        self.action_text_inactive = "бездействует"
        #self.model_prefix = f"Модель военного корабля, вооружение: {self.weapon}"
class Cargo_ship(Ship):
    def __init__(self, model, load):
        super().__init__(model)
        self.load = load
        self.action_text_active = "загружается"
        self.action_text_inactive = "разгружается"
        #self.model_prefix = f"Модель грузового корабля, груз: {self.load}"


#использование
this_object = Cargo_ship('sw9669', 'контейнеры')
two_object = Warrior_ship('esmusa', 'пушки')
this_object.action()
two_object.action()
print("Меняем статусы:")
this_object.set_action_status(False)  #грузовой корабль разгружается
two_object.set_action_status(False)   #военный корабль бездействует

this_object.action()
two_object.action()

# Дополнительные примеры
print("\nДополнительные тесты:")
three_object = Ship('обычный_корабль')
three_object.action()

print("Меняем статусы:")
three_object.set_action_status(False)
three_object.action()





