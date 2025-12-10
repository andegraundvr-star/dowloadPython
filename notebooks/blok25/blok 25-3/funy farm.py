#Весёлая ферма
class Potato:
    potato_types = {1:'Белая', 2:'Ранняя', 3: 'Голден', 4:'Кристал', 5:'Королева Анна', 6:'Синяя'}  #сорт для картошки в грядке
    stad_compleate = {1:'Росток', 2:'Зеленая', 3: 'Зрелая', 4:'Собрали'} #стадия зрелости для картошки
    total_planted = 0  # счетчик посаженных картошек
    #создаем функцию добавления количества новых посадок картошки
    def __init__(self, sort_number=1):
        Potato.total_planted += 1  #увеличиваем счетчик посадки сортов при создании
        self.potato_id = Potato.total_planted  # уникальный ID картошки
        self.sort_number = sort_number if sort_number in Potato.potato_types else 1
        self.current_stage = 1  # текущая стадия роста
        print("\nПосажена картошка #{} сорта :{} с текущем статусом '{}' ".format(
            self.potato_id,Potato.potato_types[self.sort_number], Potato.stad_compleate[self.current_stage]))
    #создаем функцию изменения стадий роста картошки
    def upgrade(self):
        while True:
                upgrade = input("Введите 'yes', если хотите чтоб картошка #{} подросла: ".format(self.potato_id))
                if upgrade == 'yes':
                    if self.current_stage < 4:
                        self.current_stage += 1
                        print("У картошки #{} ({}) "
                              "текущее состояние: '{}'".format(self.potato_id, Potato.potato_types[self.sort_number],Potato.stad_compleate[self.current_stage]))
                elif upgrade == 'no':
                    print("У картошки #{} ({}) "
                          "текущее состояние: '{}'".format(self.potato_id, Potato.potato_types[self.sort_number],Potato.stad_compleate[self.current_stage]))
                    break
                else:
                    print("Ошибка: введите только 'yes' или 'no'!")

class Garden_of_potato:
    total_garden = 'грядка одна единственная и уникальная'  #номер самой грядки
    #создаем функцию инициализации грядки
    def __init__(self):
        self.garden_nomber = Garden_of_potato.total_garden  #уникальный номер грядки
        self.list_potato = [] #грядка содержит список картошки
    #создаем функцию списка картошки
    def add_potato(self, potato):
        self.list_potato.append(potato) #Добавляем картошку в список грядки
        print(f"\nНа грядке #{self.garden_nomber} растет картошка #{potato.potato_id} "
              f"сорта '{Potato.potato_types[potato.sort_number]}' "
              f"с текущим статусом '{Potato.stad_compleate[potato.current_stage]}'")

    #создаем функцию количество посадок на грядке
    def total(self):
        print(f"На грядке #{self.garden_nomber} посажено {len(self.list_potato)} картошки: "
              f"{[p.potato_id for p in self.list_potato]}")
    #создаем функцию взращивания картошки
    def garden_update(self):
        look_potato_up = input("Введите 'yes', если все сорта картошки подросли: ")
        if look_potato_up == 'yes':
            for i in self.list_potato:
                if i.current_stage < 4:
                    i.current_stage += 1
                print(f"У картошки #{i.potato_id} ({Potato.potato_types[i.sort_number]}) "
                      f"текущее состояние: '{Potato.stad_compleate[i.current_stage]}'")
        else:
            print("Картошка не изменила своего состояния")
#создаем экземпляр грядки
garden = Garden_of_potato()

#создаем и добавляем картошку разных сортов
potato1 = Potato(sort_number=1)  # Белая
garden.add_potato(potato1)
potato1.upgrade()

potato2 = Potato(sort_number=3)  # Голден
garden.add_potato(potato2)
potato2.upgrade()

potato3 = Potato(sort_number=2)  # Ранняя
garden.add_potato(potato3)
potato3.upgrade()

potato4 = Potato(sort_number=5)  # Королева Анна
garden.add_potato(potato4)
potato4.upgrade()

#проверяем грядку
garden.total()
garden.garden_update()