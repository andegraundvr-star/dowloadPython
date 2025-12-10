#анализ цен
import random
#составляем начальный список с помощью метода рандом
original_prices = [random.randint(-12,12) for i in range(5)]
print('оригинальный список цен', original_prices)
#копируем созданный список
new_prices = original_prices[:]
#зануляем отрицательные элементы
new_prices[:] = [x if x >= 0 else 0 for x in new_prices]
print('отредактированный список цен', new_prices)
#вычитаем из суммы значений первого списка сумму значений второго списка
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))