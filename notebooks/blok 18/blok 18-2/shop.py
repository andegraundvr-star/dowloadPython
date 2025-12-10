#магазин
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#заменяем минусовые значения на нулевые и выводим новый список
new_prices = [(int(abs(x * 0)) if x < 0 else x) for x in original_prices]
print(new_prices)