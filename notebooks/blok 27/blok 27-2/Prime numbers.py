#Простые числа

#функция проверяет, является ли число простым
def _is_prime( num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_generator(start=0):
    current = start
    while True:
        if _is_prime(current):
            yield current
        current += 1

# Бесконечный вывод
gen = count_generator()
try:
    while True:
        prime = next(gen)
        print(prime)
        #Можно добавить задержку, чтобы вывод был медленнее
        import time
        time.sleep(1)
except KeyboardInterrupt:
    print("\nГенератор остановлен")
