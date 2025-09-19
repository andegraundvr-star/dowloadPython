#По парам
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_puple = []
#беерм цикл пеербора индексов по условию длинны списка
for idx in range(0, len(original_list)-1, 2):
    if idx+1 < len(original_list):
        new_puple.append((original_list[idx], original_list[idx+1]))
print(f"Список кортежей: {new_puple}")
#через zip со срезами по четным и не четным индексам
new_puple = list(zip(range(len(original_list))[0::2], (range(len(original_list))[1::2])))
print(f"Второй способ через zip: {new_puple}")
