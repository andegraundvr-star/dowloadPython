# Паранойя
import os
#для шифра Цезаря добавляем алфавиты
alphabet_hight = [chr(i) for i in range(65, 90)]
alphabet_low = [chr(i) for i in range(97, 122)]

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
    #если символ не в алфавите, оставляем как есть
    return simbol

#открываем файл для записи всех слов
with open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\06_paranoia\text.txt', 'r', encoding='utf-8') as file_from:
    N = 0
    #сохраняем содержимое в файл
    with open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\06_paranoia\cipher_text.txt', 'w', encoding='utf-8') as file_to:
        for line in file_from:
            N += 1
            #создаем новый список с символами после сдвига
            code = [caesar_char(x, N) for x in line]
            #переводим список в строку
            code_str = ''.join(code)
            file_to.write(code_str)
