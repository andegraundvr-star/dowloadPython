#простая программа

#пути к файлам
input_path = r'C:\Root\RemoteFolders\user0907\companyfrontdesc1\simple.txt'

def cleanup_temp_files():
    """Функция для очистки временных файлов (заглушка)"""
    print("Выполняется очистка временных файлов...")


#открываем файл чтения содержимого первого файла и последующей перезаписи
try:
    #сначала читаем существующее содержимое (если файл есть)
    try:
        with open(input_path, 'r', encoding='utf-8') as file_from:
            existing_content = file_from.read()
            print(f"Текущее содержимое файла:\n{existing_content}")

    except FileNotFoundError:
        print(f"  Ошибка: директория не найдена")
    except PermissionError:
        print(f"  Ошибка: нет доступа к директории")
    except UnicodeDecodeError:
        print(f"  Ошибка: файл {input_path} не текстовый или имеет другую кодировку")
    else:
        #получаем новый текст от пользователя
        people_text = input('Введите фразу для записи в файл: ')

    #записываем новый текст в файл
    try:
        with open(input_path, 'w', encoding='utf-8') as file_to:
            file_to.write(people_text)
            print("Фраза успешно записана в файл")
    except PermissionError:
        print("Ошибка: нет прав на запись в файл")
    except Exception as e:
        print(f"Неожиданная ошибка при записи: {str(e)}")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
finally:
    try:
        cleanup_temp_files()
        print("Операция завершена (успешно или с ошибкой)")
    except Exception as e:
        print(f"Ошибка при завершении: {e}")
