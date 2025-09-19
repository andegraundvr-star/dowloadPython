
#счастливая ферма 2
import random
#создаем класс картошки
class Potato:
    __potato_types = {1:'Белая', 2:'Ранняя', 3: 'Голден', 4:'Кристал', 5:'Королева Анна', 6:'Синяя'}  #сорт для картошки в грядке
    __stad_compleate = {1:'Росток', 2:'Зеленая', 3: 'Зрелая', 4:'Собрали'} #стадия зрелости для картошки
    total_planted = 0  #счетчик посаженных картошек
    #создаем функцию добавления количества новых посадок картошки
    def __init__(self, sort_number=1):
        Potato.total_planted += 1  #увеличиваем счетчик посадки сортов при создании
        self.potato_id = Potato.total_planted  # уникальный ID картошки
        self.sort_number = sort_number if sort_number in Potato.__potato_types else 1
        self.current_stage = 1  #текущая стадия роста
        print(f"Посажена картошка #{self.potato_id} сорта: {self.get_sort_name()} с текущим статусом '{self.get_stage_name()}'")
    #для доступа к защищенным данным используются геттеры
    def get_sort_name(self):
        return self.__potato_types.get(self.sort_number, "Неизвестный сорт")
    def get_stage_name(self):
        return self.__stad_compleate.get(self.current_stage, "Неизвестная стадия")
    #создаем функцию изменения стадий роста картошки
    def upgrade(self, was_cared):
        if was_cared:
            if self.current_stage < 4:
                self.current_stage += 1
                print(f"У картошки #{self.potato_id} ({self.get_sort_name()}) "
                      f"текущее состояние: '{self.get_stage_name()}'")
            else:
                print(f"Картошка #{self.potato_id} ({self.get_sort_name()}) уже созрела!")
        else:
            print(f"Картошка #{self.potato_id} ({self.get_sort_name()}) не получила ухода")
#создаем класс грядки
class Garden_of_potato:
    #создаем функцию инициализации грядки
    def __init__(self):
        self.total_garden = 'грядка одна единственная и уникальная'  #номер самой грядки
        self.list_potato = [] #грядка содержит список картошки
    #создаем функцию списка картошки
    def add_potato(self, potato):
        self.list_potato.append(potato) #Добавляем картошку в список грядки

    #создаем функцию количество посадок на грядке
    def show_status(self):
        print(f"\nСтатус грядки '{self.total_garden}':")
        print(f"Всего посажено картошки: {len(self.list_potato)}")
        for potato in self.list_potato:
            print(f"Картошка #{potato.potato_id}  ({potato.get_sort_name()}): {potato.get_stage_name()}")

    #создаем функцию взращивания картошки
    def garden_update(self, gardener):
        print(f"\nСадовник {gardener.name} ухаживает за грядкой...")
        #садовник решает, ухаживать ли за грядкой в целом
        if gardener.decide_to_care():
            print("Садовник решил ухаживать за грядкой сегодня!")
            #для каждой картошки индивидуально решается, получила ли она уход
            for potato in self.list_potato:
                cared = gardener.care_for_potato()
                potato.upgrade(cared)
        else:
            print("У садовника сегодня выходной, он не ухаживает за грядкой")
            for potato in self.list_potato:
                potato.upgrade(False)

class Thelawnmower:
    def __init__(self, name='Thelawnmower'):
        self.name = name
        print(f"\nПривет, я садовник {self.name}")
    def decide_to_care(self):
        #садовник решает, ухаживать ли за грядкой сегодня с вероятностью 70%
        return random.random() < 0.7
    def care_for_potato(self):
        #для каждой картошки индивидуально решается, получила ли она уход с вероятностью 80%
        return random.random() < 0.8
#создаем экземпляр грядки
garden = Garden_of_potato()
gardener = Thelawnmower('Thelawnmower')

#создаем и добавляем картошку
potatoes = [
    Potato(sort_number=1),
    Potato(sort_number=3),
    Potato(sort_number=2),
    Potato(sort_number=5)
]

for potato in potatoes:
    garden.add_potato(potato)

#ухаживаем за грядкой в течение 3 дней
for day in range(3):
    print(f"\n=== День {day+1} ===")
    garden.garden_update(gardener)

#проверяем грядку
garden.show_status()