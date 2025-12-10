
# Паранойя 2
import os
#для шифра Цезаря добавляем алфавиты
alphabet_hight = [chr(i) for i in range(65, 90)]
alphabet_low = [chr(i) for i in range(97, 122)]
alphabet_Rus = [chr(i) for i in range(1040, 1104)]
#функция - заглушка
def cleanup_temp_files():
    print("Выполняется очистка временных файлов...")

#создаем функцию для шифрования одного символа
def caesar_char(simbol, N):
    if simbol in alphabet_hight:
        original_index = alphabet_hight.index(simbol)
        index = (alphabet_hight.index(simbol) + N) % len(alphabet_hight)

        return alphabet_hight[index]
    elif simbol in alphabet_low:
        original_index = alphabet_low.index(simbol)
        index = (alphabet_low.index(simbol) + N) % len(alphabet_low)

        return alphabet_low[index]
    elif simbol in alphabet_Rus:
        original_index = alphabet_Rus.index(simbol)
        index = (alphabet_Rus.index(simbol) + N) % len(alphabet_Rus)

        return alphabet_Rus[index]
    #если символ не в алфавите, оставляем как есть
    return simbol

open_file = r'C:\Root\RemoteFolders\user0907\companyfrontdesc1\simple.txt'


try:
    #открываем файл для записи всех слов
    with open(open_file, 'r', encoding='utf-8') as file_from:
        N = 0
        #сохраняем содержимое в файл
        with open(r'C:\Root\RemoteFolders\user0907\companyfrontdesc1\simple_change.txt', 'w', encoding='utf-8') as file_to:
            for line in file_from:
                N += 1
                #создаем новый список с символами после сдвига
                code = [caesar_char(x, N) for x in line]
                #переводим список в строку
                code_str = ''.join(code)
                file_to.write(code_str)
except FileNotFoundError:
    print(f"  Ошибка: директория не найдена")
except PermissionError:
    print(f"  Ошибка: нет доступа к директории")
except UnicodeDecodeError:
    print(f"  Ошибка: файл {open_file} не текстовый или имеет другую кодировку")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
else:
    #выводим результат работы кода
    print("\nполученный результат:")
    #for item in code_str:
    print(code_str)
finally:
    try:
        cleanup_temp_files()
        print("Операция завершена")
    except Exception as e:
        print(f"Ошибка при завершении: {e}")

