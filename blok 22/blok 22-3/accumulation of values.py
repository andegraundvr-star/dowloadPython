#Накопление значений
#для работы с изменяемыми объектами типо списков
def build_function(num, new_list=None): #передаем вторым аргументом значение по умолчанию  none
    #в теле функции задаем список заново и добавляем в него первый аргумент
    if new_list is None:
        new_list = []
    new_list.append(num)
    print("new_list", new_list)

build_function(5)
build_function(10)
build_function(15)