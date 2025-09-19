#возврат
import os
from datetime import datetime
#добавляем алфавиты для присваивания опеределенных символов строкам
alphabet_En = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

#создаем функцию для редактирования строк
def redact_text(file_line, index):
    try:
        #преобразуем строку в число (если это возможно)
        num = int(file_line.strip())
        #берем символ из алфавита по модулю длины алфавита (чтобы избежать IndexError)
        i_elem = alphabet_En[num % len(alphabet_En)]

        return i_elem
    except ValueError:
        print(f"Ошибка: '{file_line.strip()}' не является числом")
        return None

#пути к файлам
input_path = r'C:\Root\RemoteFolders\user0907\companyfrontdesc1\ages.txt'
output_path = r'C:\Root\RemoteFolders\user0907\companyfrontdesc1\result.txt'
#открываем файл чтения содержимого первого файла и последующей перезаписи
try:
    #проверяем существование выходного файла
    if os.path.exists(output_path):
        #генерируем уникальное имя файла с timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_output_path = f"{output_path.split('.')[0]}_{timestamp}.txt"
        print(f"Файл {output_path} уже существует. Создаем новый файл: {new_output_path}")
        output_path = new_output_path
    with open(input_path, 'r', encoding='utf-8') as file_from:
        #сохраняем содержимое в файл
        with open(output_path, 'w', encoding='utf-8') as file_to:

            #словарь для хранения результатов
            ages_book = {}

            #обрабатываем каждую строку из входного файла
            for idx, line in enumerate(file_from):
                if line.strip():  #пропускаем пустые строки
                    #преобразуем строку с помощью функции redact_text
                    result = redact_text(line, idx)
                    if result is not None:
                        #записываем в словарь и в файл
                        ages_book[line.strip()] = result
                        file_to.write(f"{line.strip()}: {result}\n")
                        #print(f'Добавлено: {line.strip()} - {result}')
except FileExistsError:
    print("Ошибка: файл уже существует и не может быть перезаписан")
except FileNotFoundError:
    print(f"  Ошибка: директория не найдена")
except PermissionError:
    print(f"  Ошибка: нет доступа к директории")
except UnicodeDecodeError:
    print(f"  Ошибка: файл {file_from} не текстовый или имеет другую кодировку")
else:
    #выводим итоговый словарь
    print("\nИтоговый словарь:")
    for key, value in ages_book.items():
        print(f"{key}: {value}")

