#Простые числа
#класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N
class Primes:
    def __init__(self, n):
        self.n = n #на входе получаем максимальное число, которое будем раскладывать на простые числа
        self.current = 1  #начинаем с 1
    def __iter__(self):
        self.current = 1 #текущее значение
        return self
    #функция проверяет, является ли число простым
    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def __next__(self):
        self.current += 1
        while self.current <= self.n:
            if self._is_prime(self.current):
                return self.current
            self.current += 1
        raise StopIteration
#использование - создаем экземпляр, на воходе количество индексов в списке
iterator = Primes(44)
print("Простые числа дo 44:", list(iterator))
#вызываем метод класса еще раз с другим количеством элементов
iterator2 = Primes(88)
print("Простые числа до 88:", list(iterator2))