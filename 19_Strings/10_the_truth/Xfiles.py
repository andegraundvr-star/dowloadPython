# Истина (другой вариант)
import re
thrue_shift = 25 #предполагаемый сдвиг по Цезарю
#исходный зашифрованный текст
frase = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

#разбиваем текст, сохраняя пробелы (используем findall вместо split)
frase_parts = re.findall(r'(\S+|\s)', frase)

#добавляем алфавиты
alphabet = [chr(i) for i in range(97, 123)]  # a-z
alphabet_high = [chr(i) for i in range(65, 91)]  # A-Z

#переворачиваем каждое слово
reversed_text = [''.join(reversed(part)) for part in frase_parts]
mem_text = ''.join(reversed_text)
print('Перевернутый текст:', mem_text)

#функция для шифрования Цезаря
def caesar_char(simbol, shift):
    if simbol.islower() and simbol in alphabet:
        index = (alphabet.index(simbol) + shift) % len(alphabet)
        return alphabet[index]
    elif simbol.isupper() and simbol in alphabet_high:
        index = (alphabet_high.index(simbol) + shift) % len(alphabet_high)
        return alphabet_high[index]
    return simbol

#пробуем разные сдвиги
for shift in range(1, 26):
    decoded = [caesar_char(c, shift) for c in mem_text]
    print(f'Сдвиг {shift}:', ''.join(decoded))
frase_thrue = ''.join([caesar_char(c, thrue_shift) for c in mem_text])
#нашли фразу, которую будем преобразовывать

print(frase_thrue)

def move_slash_to_end(word):

    letters = [c for c in word if c != '/']
    slashes = [c for c in word if c == '/']
    return ''.join(letters + slashes)

def process_word(word, shift_pos):

    if len(word) > shift_pos:
        return word[shift_pos] + word[:shift_pos][::-1] + word[shift_pos+1:][::-1]
    return word[::-1]

#перемещаем '/' в конец каждого слова
processed_words = [move_slash_to_end(word) for word in frase_thrue.split()]
modified_text = ' '.join(processed_words)

#разделяем текст по '/'
parts = modified_text.split('/')

#ручной ввод сдвигов для каждого этапа
shifts = []
#print("Укажите сдвиги для каждого этапа обработки (начиная с 0):")
#for i in range(len(parts)):
#    shift = int(input(f"Сдвиг для этапа {i+1} (часть {i}): "))
#    shifts.append(shift)
#ввод сдвигов списком
shifts = [2,3,4,5,-2,1,8,2,2,11,2,3,5,7,4,1,4,4,0]
#обработка каждой части с заданным сдвигом
results = []
for i, (part, shift) in enumerate(zip(parts, shifts)):
    processed_part = ' '.join(process_word(word, shift) for word in part.split())
    results.append(processed_part)
    print(f'\nЭтап {i+1} (сдвиг {shift}):')
    print(processed_part)

#сборка финального результата
final_result = '/'.join(results)
print("\nФинальный результат:")
print(final_result)

after_check_net ="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
