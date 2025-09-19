#Сервер
server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

for i_server, i_dict in server_data.items():
    #мечатаем только первую переменную
    print(f"{i_server}:")
    #запускаем вложенный цикл, проходим по значеиням словаря
    for i_item, i_conf in i_dict.items():
        #печатаем ключ - значение
        print(f"      {i_item} : {i_conf}")
