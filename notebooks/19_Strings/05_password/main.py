# Пароль
password = input('введите сложный пароль: ')

#проверяем наличие специальных символов
has_symbols = any(symbol in password for symbol in '@№$%^&*()!"#;:?')
#проверяем наличие заглавных букв
has_upper = any(symbol.isupper() for symbol in password)
#проверяем наличие цифр
digit_count = sum(1 for num in password if num in '0123456789')
#проверяем наличие латинских букв (строчных или заглавных)
eng_alphabet = any(sym.isalpha() and sym.lower() in 'abcdefghijklmnopqrstuvwxyz' for sym in password)
#проверяем на минимальную длинну
has_lonner = len(password) >= 8

if has_symbols and digit_count >= 3 and has_upper and eng_alphabet and has_lonner:
    print('Отлично! Пароль сложный.')
else:
    print('Пароль недостаточно сложный. Нужно:')
    if not has_symbols:
        print('- хотя бы один специальный символ (@, №, $, %, ^, &, *, ( , )')
    if digit_count < 3:
        print('- необходимо три цифры')
    if not has_upper:
        print('- хотя бы одна заглавная буква')
    if not eng_alphabet:
        print('- буквы должны быть из латинского алфавита')
    if not has_lonner:
        print('- пароль должен быть не менее 8 символов')

