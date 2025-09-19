#лавка
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('введите новый фрукт: ')
price = int(input('укажите цену: '))

goods.append([fruit_name, price])
for item in goods:
    item[1] = round(item[1] * 1.08, 2)
print(goods)