# Клетки
quantity = int(input('введите количество: '))
list_of_cells = []
for i in range(quantity):
    print('клетка с индексом: ', i + 1, 'и ее эффектисность: ', end = '')
    cell_efficiency = input()
    if i > int(cell_efficiency):
        list_of_cells.append(i)
print('список не подходящих к эксперименту клеток:', list_of_cells)
