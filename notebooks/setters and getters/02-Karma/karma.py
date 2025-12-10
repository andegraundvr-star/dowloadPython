#карма
import random
import os

#задаем путь к файлам для записи логов
base_dir = r"C:\Root\RemoteFolders\user0907"
output_path = os.path.join(base_dir, 'python-ds', 'setters and getters', '02-Karma')
output_file_bad = os.path.join(output_path, 'lucky.log')

#задаем классы исключений
class KillError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass
class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass

class RandomError:
    #создаем функцию выбора класса случайной ошибки
    @staticmethod
    def raise_exception():
        exceptions = [
            KillError,
            DrunkError,
            CarCrashError,
            GluttonyError,
            DepressionError
        ]
        return random.choice([exceptions])

#создаем основной класс
class Persone:
    total_karma = 0
    total_day = 0
    def __init__(self):
        self.errors_log = []  #список для хранения ошибок
    def one_day(self,how_match_karma=0):
        #основной цикл дней
        while Persone.total_karma < 500:
            Persone.total_day += 1
            print(f"Наступил {Persone.total_day} день")
            try:
                #получаем карму за день
                daily_karma = random.randint(1, 7)
                #проверяем, произошло ли случайное событие (1 к 10)
                if random.choices([True, False], weights=[1, 9], k=1)[0]:
                    #вызываем случайное исключение
                    RandomError.raise_exception()

                #если исключения не было, добавляем карму
                Persone.total_karma += daily_karma
                print(f"Получено кармы: {daily_karma}, общая карма: {Persone.total_karma}")

            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                #логируем ошибку
                error_msg = f"День {Persone.total_day} ошибка: {type(e).__name__}"
                self.errors_log.append(error_msg)


        print(f"Достигнута карма {Persone.total_karma} за {Persone.total_day} дней")


    def save(self):
        #записываем ошибки в файл
        try:
            with open(output_file_bad, 'w', encoding='utf-8') as file_to_bad:
                for error in self.errors_log:
                    file_to_bad.write(error + '\n')
                    print(f'Записано в лог: {error}')
            print(f"Логи сохранены в файл: {output_file_bad}")
        except Exception as e:
            print(f"Ошибка при записи в файл: {type(e).__name__}")

#создаем экземпляр класса
this_man = Persone()
#запускаем метод дней
this_man.one_day()
#сохраняем логи
this_man.save()
