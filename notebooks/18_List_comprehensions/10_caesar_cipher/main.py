# Шифр Цезаря
line_of_caesar = input('введите строку для шифорования: ').lower()
N = int(input('введите сдвиг: '))
#создаем русский алфавит (строчные буквы)
alphabet = [chr(i) for i in range(1072, 1104)]
#print(alphabet)

#создаем функцию для шифрования одного символа
def caesar_char(simbol, N):
    if simbol in alphabet:
        original_index = alphabet.index(simbol)
        index = (alphabet.index(simbol) + N) % len(alphabet)
        #print(original_index,simbol, N, len(alphabet), index)
        return alphabet[index]
    #если символ не в алфавите , оставляем как есть
    return simbol

#создаем новый список с символами после сдвига
code = [caesar_char(x, N) for x in line_of_caesar]
#print(code)
#переводим список в строку
code_str = ''.join(code)

print('зашифрованное сообщение:', code_str)