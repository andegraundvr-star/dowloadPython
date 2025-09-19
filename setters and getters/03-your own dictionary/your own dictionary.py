#Свой словарь
#реализуем класс с наследованием от родительского dict, переопределяем метод get
class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)
#Cоздаем экземпляр MyDict
my_dict = MyDict()
my_dict['a'] = 1
my_dict['b'] = 2

#тестируем метод get
#ключ существует
print(my_dict.get('a'))
#ключ отсутствует
print(my_dict.get('c'))
#ключ отсутствует, но указано другое значение
print(my_dict.get('c', 10))