# Истина
import re

#исходный зашифрованный текст
frase = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

#добавляем алфавиты
alphabet = [chr(i) for i in range(97, 123)]  # a-z
alphabet_high = [chr(i) for i in range(65, 91)]  # A-Z

#функция для шифрования Цезаря
def caesar_char(simbol, shift):
    if simbol.islower() and simbol in alphabet:
        index = (alphabet.index(simbol) + shift) % len(alphabet)
        return alphabet[index]
    elif simbol.isupper() and simbol in alphabet_high:
        index = (alphabet_high.index(simbol) + shift) % len(alphabet_high)
        return alphabet_high[index]
    return simbol

thrue_shift = 12 #предполагаемый сдвиг по Цезарю

#пробуем разные сдвиги
for shift in range(1, 26):
    decoded = [caesar_char(c, shift) for c in frase]
    print(f'Сдвиг {shift}:', ''.join(decoded))
frase_thrue = ''.join([caesar_char(c, thrue_shift) for c in frase])
#нашли фразу, которую будем преобразовывать

print(frase_thrue)
#перемещаем '/' в конец каждого слова
def move_slash_to_end(word):

    letters = [c for c in word if c != '/']
    slashes = [c for c in word if c == '/']
    return ''.join(letters + slashes)

processed_words = [move_slash_to_end(word) for word in frase_thrue.split()]
modified_text = ' '.join(processed_words)
print(modified_text)

def move_slash_to_end(word):

    letters = [c for c in word if c != '/']
    slashes = [c for c in word if c == '/']
    return ''.join(letters + slashes)

def process_word(word, shift_pos):

    if len(word) != 2:
        return word[-shift_pos:] + word[:-shift_pos]
    if len(word) == 2:
        return word   # Для слов из 2 знаков
    if len(word) == 4:
        return word   # Для слов из 4 знаков

#перемещаем '/' в конец каждого слова
#processed_words = [move_slash_to_end(word) for word in frase_thrue.split()]
#modified_text = ' '.join(processed_words)

#разделяем текст по '/'
parts = modified_text.split('/')
#ввод сдвигов списком
shifts = [3,4,5,6,3,2,9,3,3,6,1,0,0,0,2,2,2,0,1]
#обработка каждой части с заданным сдвигом
results = []
for i, (part, shift) in enumerate(zip(parts, shifts)):
    processed_part = ' '.join(process_word(word, shift) for word in part.split())
    results.append(processed_part)
    #print(f'\nЭтап {i+1} (сдвиг {shift}):')
    print(processed_part)
final_frace = ''.join(results)


print(final_frace)

#применяем метод "rot13"
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
print('Результат после всех преобразований: ',end='')
print("".join([d.get(c, c) for c in final_frace]))


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