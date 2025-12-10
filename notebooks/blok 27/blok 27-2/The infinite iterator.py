#бесконечный счетчик

class CountIterator:
    def __init__(self):
        self.count = 0 #задаем только один статический атрибут - счетчик
    def __iter__(self):
        self.current = 0 #текущее значение
        return self
    def __next__(self):
        #условия для стопа итерации нет
        self.current +=1
        return self.current - 1 #выводим предыдущий элемент

#использование - создаем экземпляр
my_iter = CountIterator()
#проходим циклом по экземпляру
for i_elem in my_iter:
    print(i_elem)
