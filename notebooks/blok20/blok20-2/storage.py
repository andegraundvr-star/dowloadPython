#Склады
small_storage = {

    'гвозди': 5000,

    'шурупы': 3040,

    'саморезы': 2000

}



big_storage = {

    'доски': 1000,

    'балки': 150,

    'рейки': 600

}
#объединяем словари
big_storage.update(small_storage)
print(big_storage)
#создаем цикл поиска товара по имени и вывод значения по ключу с попмощью метода get
for i in big_storage:
    name = input('введите название товара: ')
    print(big_storage.get(name))
