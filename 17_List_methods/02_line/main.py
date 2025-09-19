#  Шеренга

klass_A = (list(range(160, 176 + 1, 2)))
klass_B = (list(range(162, 180 + 1, 3)))
print('Класс A: ',klass_A)
print('Класс B: ',klass_B)
combined = klass_A + klass_B
combined.sort()
print("Объединенный и отсортированный список:", combined)