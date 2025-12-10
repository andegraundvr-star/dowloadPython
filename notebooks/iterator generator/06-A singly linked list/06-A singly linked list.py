#Односвязный список
"""Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.

Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.


В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:

append — добавление элемента в конец списка;
get — получение элемента по индексу;
remove — удаление элемента по индексу.
Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

Результат:
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]"""



#yзел односвязного списка
class Node:
    def __init__(self, data):
        self.data = data  #данные узла
        self.next = None  #ссылка на следующий узел или None, если это последний узел
#односвязный список
class LinkedList:
    def __init__(self):
        self.head = None  #первый узел списка
        self.length = 0   #длина списка
    #метод создания нового узла
    def append(self, data):
        #добавление элемента в конец списка
        new_node = Node(data)
        if self.head is None:
            #если список пустой, новый узел становится головным
            self.head = new_node
        else:
            #если не пустой: находим последний узел и добавляем новый после него
            current = self.head
            while current.next is not None:
                current = current.next
            #добавляем новый узел в конец
            current.next = new_node
        #увеличиваем длинну списка
        self.length += 1
    #метод проверяет корректность индекса
    def get(self, index):
        #ищем индекс в не длинны списка и возращаем ошибку
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        #или возращаем корректные данные узла
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    #удаление элемента по индексу
    def remove(self, index):
        #проверяет корректность индекса при удалении элементов из списка
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        if index == 0:
            #удаляем головной элемент
            self.head = self.head.next
        else:
            #находим узел перед удаляемым
            current = self.head
            for _ in range(index - 1):
                current = current.next
            #пропускаем удаляемый узел
            current.next = current.next.next
        #уменьшаем длинну списка
        self.length -= 1
    #делаем объект итерируемым
    def __iter__(self):
        #Итератор для обхода списка
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    #cтроковое представление списка
    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return '[' + ', '.join(elements) + ']'
    #метод возвращает длину списка
    def __len__(self):
        return self.length

#создаем экземпляр объекта
my_list = LinkedList()
#добавляем узлы
my_list.append(10)
my_list.append(20)
my_list.append(30)

print('Результат:', my_list)
#выводим элемент списка
print('Получение третьего элемента:', my_list.get(2))
#удаляем элемент
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
