#создание графика работы
import os
from pathlib import Path
#задаем путь к файлу
# Или для общей папки Documents:
base_dir = r"C:\Users\user0907\documents"
path_file = os.path.join(base_dir, 'people.txt')
import sys


if sys.version_info < (3, 6):
    print("Требуется Python 3.6 или выше!")
    sys.exit(1)

from datetime import date
#Получаем дату через 2 месяца от текущей
today = date.today()
year = today.year
month = today.month

# Корректируем год, если месяц +2 выходит за пределы 12
if month + 2 > 12:
    year += 1
    month = (month + 2) - 12
else:
    month += 2
import calendar
days_in_month = calendar.monthrange(year, month)[1]
#print(days_in_month)
# Получаем матрицу календаря месяца (недели в строках)
month_calendar = calendar.monthcalendar(year, month)

# Воскресенья находятся в последнем столбце (индекс 6)
sundays = [
    week[6]
    for week in month_calendar
    if week[6] != 0  # Игнорируем нули (дни из других месяцев)
]

# Формируем надпись
month_name = date(year, month, 1).strftime('%B')  # Получаем название месяца
print(f"Воскресенья в {month_name} {year}: {'; '.join(map(str, sundays))}")


line_work = [12,4,"-","-"]
body_2 = ["-", 12,4,"-"]
body_3 = ["-","-",12,4]
body_4 = [4,"-","-",12]
def duble(list):
    while len(list) < days_in_month:
        list += list
    line_work_31 = (list)[:days_in_month]
    # Заменяем '-' на 'B' в воскресенья
    for i in range(len(line_work_31)):
        if (i+1) in sundays and line_work_31[i] == '-':  # i+1 потому что дни месяца начинаются с 1
            line_work_31[i] = 'B'
    #заменяем первую 4 в графике на 0
    if line_work_31[0] == 4:
        line_work_31[0] = 0
    # Добавляем "8" после каждого "4"
    new_list = []
    for item in line_work_31:
        new_list.append(item)
        if item == 4:
            new_list.append(8)
            
    # Обрезаем до нужной длины, если добавили лишние элементы
    return new_list[:days_in_month]

kashey_bessmertny = duble(line_work)
kashey_bessmertny_sum_11 = sum(x for x in kashey_bessmertny if x == 12 or x == 4 or x == 8)
kashey_bessmertny_sum_8 = sum(x for x in kashey_bessmertny if x == 8)
# Добавляем сумму в конец списка
kashey_bessmertny.insert(0, "kashey_bessmertny")
kashey_bessmertny.append(kashey_bessmertny_sum_11)
kashey_bessmertny.append(kashey_bessmertny_sum_8)

baba_yaga = duble(body_2)
baba_yaga_sum_11 = sum(x for x in baba_yaga if x == 12 or x == 4 or x == 8)
baba_yaga_sum_8 = sum(x for x in baba_yaga if x == 8)
# Добавляем сумму в конец списка
baba_yaga.insert(0, "baba_yaga")
baba_yaga.append(baba_yaga_sum_11)
baba_yaga.append(baba_yaga_sum_8)


ivan_tsarevich = duble(body_3)
ivan_tsarevich_sum_11 = sum(x for x in ivan_tsarevich if x == 12 or x == 4 or x == 8)
ivan_tsarevich_sum_8 = sum(x for x in ivan_tsarevich if x == 8)
# Добавляем сумму в конец списка
ivan_tsarevich.insert(0, "ivan_tsarevich")
ivan_tsarevich.append(ivan_tsarevich_sum_11)
ivan_tsarevich.append(ivan_tsarevich_sum_8)

tsarevna_lyagushka = duble(body_4)
tsarevna_lyagushka_sum_11 = sum(x for x in tsarevna_lyagushka if x == 12 or x == 4 or x == 8)
tsarevna_lyagushka_sum_8 = sum(x for x in tsarevna_lyagushka if x == 8)
# Добавляем сумму в конец списка
tsarevna_lyagushka.insert(0, "tsarevna_lyagushka")
tsarevna_lyagushka.append(tsarevna_lyagushka_sum_11)
tsarevna_lyagushka.append(tsarevna_lyagushka_sum_8)

# Форматируем вывод через точку с запятой
def format_output(lst):
    return ';'.join(map(str, lst))
# Выводим результаты
print("kashey_bessmertny:", format_output(kashey_bessmertny))
print("baba_yaga:", format_output(baba_yaga))
print("ivan_tsarevich:", format_output(ivan_tsarevich))
print("tsarevna_lyagushka:", format_output(tsarevna_lyagushka))

#чтение файла
try:

    with open(path_file, 'w', encoding='utf-8') as file_graphic:
        file_graphic.write(f"Воскресенья в {today.strftime('%B %Y')}: {sundays}\n")
        file_graphic.write(f"{format_output(kashey_bessmertny)}\n")
        file_graphic.write(f"{format_output(baba_yaga)}\n")
        file_graphic.write(f"{format_output(ivan_tsarevich)}\n")
        file_graphic.write(f"{format_output(tsarevna_lyagushka)}\n")

except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("\nРабота программы завершена")


