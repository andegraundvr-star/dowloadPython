#Однотипные объекты
#создаем класс по телевизорам
class Televisor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60
    #создаем функцию изменения параметров
    def __init__(self,freq=60):
        self.freq = freq
    #создаем функцию вывода информации о предмете
    def info(self):
        print("\nТелевизор:")
        print(f"Производитель: {self.name}")
        print(f"Матрица: {self.matrix}")
        print(f"Разрешение: {self.res}")
        print(f"Частта обновления: {self.freq} Гц")
#создаем экземпляры с разными параметрами
televisor_1 = Televisor(freq=144)
televisor_2 = Televisor(freq=70)
televisor_3 = Televisor()
televisor_4 = Televisor()
#выводим информацию
televisor_1.info()
televisor_2.info()
televisor_3.info()
televisor_4.info()
#создаем класс по наушникам
class Headphones:
    name = 'Sony'
    sensitivity = 108
    headphones_micro = 'no'
    #создаем функцию изменения параметров
    def __init__(self,headphones_micro='no'):
        self.headphones_micro = headphones_micro
    #создаем функцию вывода информации о предмете
    def info(self):
        print("\nНаушники:")
        print(f"Производитель: {self.name}")
        print(f"Чувствительность: {self.sensitivity}")
        print(f"Наличие микрофона: {self.headphones_micro}")
#создаем экземпляры с разными параметрами
headphones_1 = Headphones()
headphones_2 = Headphones(headphones_micro='yes')
headphones_3 = Headphones(headphones_micro='yes')
#выводим информацию
headphones_1.info()
headphones_2.info()
headphones_3.info()