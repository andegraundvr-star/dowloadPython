# Чат
import os

#задаем путь к файлу
base_dir = r"C:\Root\RemoteFolders\user0907"
path_dir = os.path.join(base_dir, 'python-ds', '24_Exceptions', '06_chat')
path_file = os.path.join(path_dir, 'chat.txt')

#функция логин и пароль
def log_pass(login,password):
    credentials = {
        'Volodya': 'первый',
        'user1': 'qwerty'
    }
    if login in credentials and credentials[login] == password:
        print("Вход разрешен")
        return True
    else:
        raise Exception("Неверный логин или пароль")

#чтение файла
try:
    with open(path_file, 'r', encoding='utf-8') as file_chat:
        #выводим сообщения в чате
        for line in file_chat:
            print(line.strip())
    #добавляем условие записи в файл
    login = input('\nвведите логин: ')
    password = input('введите пароль: ')
    if log_pass(login,password):
        while True:
            message = input('\nВведите сообщение или "exit" для выхода: ')
            if message.lower() == 'exit':
                break
            #сохраняем новое содержимое в файлы
            with open(path_file, 'w', encoding='utf-8') as file_to:
                file_to.write(f"{login}: {message}\n")
                print(f'Добавлено в чат: {login}: {message}')
except FileNotFoundError:
    print(f"Ошибка: файл {path_file} не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("\nРабота программы завершена")