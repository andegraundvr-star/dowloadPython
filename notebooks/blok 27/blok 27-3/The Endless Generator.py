#Бесконечный генератор
#генераторная функция
def count_generator(start=0):
    current = start
    while True:
        yield current
        current += 1

# Бесконечный вывод
gen = count_generator()
while True:
    print(next(gen))