#Компания
import random

class Person:
    def __init__(self, name, second_name, old):
        self.__name = name
        self.__second_name = second_name
        self.__old = old

    #геттеры для доступа к приватным полям
    def get_name(self):
        return self.__name
    def get_second_name(self):
        return self.__second_name
    def get_old(self):
        return self.__old
#создаем новый класс, наследуем от Person
class Employee(Person):
    def __init__(self, name, second_name, old):
        super().__init__(name, second_name, old)
        self.hours_worked = 0
    def set_hours_worked(self):
        self.hours_worked = random.randint(155, 180)
        return self.hours_worked
    def calculation(self):
        return 13000 #базовая зп , она же зп менеджера
#создаем дочерние классы, наследуем от Employee
class Manager(Employee):
    def calculation(self):
        return super().calculation()  #используем базовую зарплату
class Agent(Employee):
    def calculation(self):
        wage = 5000
        sales_volume = random.randint(20000, 50000) #задаем рандомный объем продаж
        return wage + sales_volume * 0.05  #5% от объема продаж
class Worker(Employee):
    def calculation(self):
        hours = self.set_hours_worked()  #получаем количество часов
        return 100 * hours #выводим зп рабочего

#создаем список объектов классов и вызываем зарплату
employees = [
    Manager('Edvard', 'Shevron', 61),
    Manager('Roberto', 'Carloss', 55),
    Manager('Enrikee', 'Egleseyas', 50),
    Agent('Djon', 'Smitt', 60),
    Agent('Bond', 'James', 49),
    Agent('lesley', 'Ninsen', 59),
    Worker('Silwestor', 'Stallone', 58),
    Worker('Marshal', 'Meters', 56),
    Worker('Bob', 'Torton', 54)
]

#выводим информацию о зарплате каждого сотрудника
for employee in employees:
    salary = employee.calculation()
    print(f"{employee.get_name()} {employee.get_second_name()}: {salary:.2f} руб.")



