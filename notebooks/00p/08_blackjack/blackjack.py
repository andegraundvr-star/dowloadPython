#Блэкджек
import random
import os
from datetime import datetime
#задаем путь к файлам для записи логов
base_dir = r"C:\Root\RemoteFolders\user0907"
output_path = os.path.join(base_dir, 'python-ds', '00p', '08_blackjack')
output_file = os.path.join(output_path, 'statistic.txt')

# Создаем папку для логов, если она не существует
os.makedirs(output_path, exist_ok=True)  # Добавлено создание папки

#создаем словарь самой главной комбинации Блек Джек
#blackjack_combinations = {1:['A','K'], 2:['A','Q'], 3:['A','J'], 4:['A','10'],5:['K','A'], 6:['Q','A'], 7:['J','A'], 8:['10','A']}
#создаем класс - список карт для Блек-Джека - 8 колод по 52 карты
class Deck:
    def __init__(self, num_decks=8):
        self.card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.card_deck_BJ = [i for i in self.card_deck for _ in range(4 * num_decks)]
        #перемешиваем и обрезаем половину коллоды
        random.shuffle(self.card_deck_BJ)
        self.our_card_deck = self.card_deck_BJ[:len(self.card_deck_BJ)//2]
    #создаем функцию вызова карты и удаления ее из общей колоды
    def deal_card(self):
        return self.our_card_deck.pop()
    #созадем класс выхода из текущего шаффла
    def answer_continue(self):
        answer = input("\nХотите сыграть еще раз? (1 - Да, 0 - Нет): ")
        return answer

#создаем класс диллера
class Dealer:
    def __init__(self):
        self.hand = []
        self.sum = 0
    #набор карт в новый список и подсчет суммы
    def take_card(self, card):
        #создаем список комбинации карт и сумму их очков
        self.hand.append(card)
        self.calculate_sum()
    #создаем функцию счета
    def calculate_sum(self):
        self.sum = 0
        #создаем счетчик тузов .чтобы потом корректировать сумму очков у диллера
        aces = 0
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                self.sum += 10
            elif card == 'A':
                self.sum += 11
                aces += 1
            else:
                self.sum += card
        #корректировка для тузов при превышении 21 очка
        while self.sum > 21 and aces  >= 1:
            self.sum -= 10
            aces -= 1
    #создаем функцию набора карт диллером
    def play_dealer(self, deck):
        while self.sum < 17:
            self.take_card(deck.deal_card())

#создаем класс игрока
class Player:
    def __init__(self):
        #создаем список комбинации карт и сумму их очков
        self.hand = []
        self.sum = 0
    #набор карт в новый список и подсчет суммы
    def take_card(self, card):
        self.hand.append(card)
        self.calculate_sum()
    #создаем функцию счета
    def calculate_sum(self):
        self.sum = 0
        #создаем счетчик тузов .чтобы потом корректировать сумму очков у игрока
        aces = 0
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                self.sum += 10
            elif card == 'A':
                self.sum += 11
                aces += 1
            else:
                self.sum += card
        #корректировка для тузов при превышении 21 очка
        while self.sum > 21 and aces >= 1:
            self.sum -= 10
            aces -= 1

#создаем класс игры
class GameSession:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def start_session(self):
        while True:
            #проверяем, достаточно ли карт в колоде
            if len(self.deck.our_card_deck) < 10:
                print("Колода заканчивается. Перемешиваем новую колоду.")
                self.deck = Deck()

            #сбрасываем руки игрока и дилера
            self.player.hand = []
            self.player.sum = 0
            self.dealer.hand = []
            self.dealer.sum = 0

            #создаем и запускаем игру
            game = GameWithExistingObjects(self.deck, self.dealer, self.player)
            game.start_game()

            #вводим условие прерывания игры с текущим шаффлом
            answer = self.deck.answer_continue()
            if answer != '1':
                print("Спасибо за игру!")
                break


#Изменил класс Game, чтобы он принимал существующие объекты
class GameWithExistingObjects:
    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.statistic_log = []  #список для хранения статистики
    #добавляем метод проверки Black Jack у игрока или у дилера
    def has_blackjack(self, hand):
        if len(hand) != 2:
            return False
        #преобразуем карты в строки
        card1, card2 = str(hand[0]), str(hand[1])
        #проверяем комбинации вместо сортировки
        return (card1 == 'A' and card2 in ['10', 'J', 'Q', 'K']) or \
            (card2 == 'A' and card1 in ['10', 'J', 'Q', 'K'])
    #создаем функцию вызова карты
    def answer_hit(self):
        answer = input("\nЕще карту? (1 - Да, 0 - Нет): ")
        return answer

    def save(self):
        try:
            # Открываем файл в режиме добавления ('a') вместо перезаписи ('w')
            with open(output_file, 'a', encoding='utf-8') as file_to:
                for next_line in self.statistic_log:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # Добавляем текущую дату и разделитель " -!- "
                    file_to.write(f"{current_time} -!- {next_line}\n")
            print(f"Логи сохранены в файл: {output_file}")
        except Exception as e:
            print(f"Ошибка при записи в файл: {type(e).__name__}")

    def start_game(self):
        print("Добро пожаловать в игру Блэкджек!")
        # Раздача первых двух карт
        self.player.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())
        self.player.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())

        player_blackjack = self.has_blackjack(self.player.hand)
        dealer_blackjack = self.has_blackjack(self.dealer.hand)

        if player_blackjack:
            if dealer_blackjack:
                print(f"\nУ вас Blackjack! {self.player.hand}")
                print(f"У дилера тоже Blackjack! {self.dealer.hand}")
                print("Ничья!")
                # Добавление записи в лог и сохранение перед выходом
                statistics_msg = f"Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
                self.statistic_log.append(statistics_msg)
                self.save()
                return
            else:
                print(f"\nУ вас Blackjack! {self.player.hand}")
                print("Вы выиграли с Blackjack!")
                dealer_first_card = self.dealer.hand[0]
                dealer_second_card = self.dealer.hand[1]
                print(f"А у дилера первая карта {dealer_first_card}, а вторая {dealer_second_card}")
                statistics_msg = f"Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
                self.statistic_log.append(statistics_msg)
                self.save()
                return

        print(f"\nВаши карты: {self.player.hand}, сумма: {self.player.sum}")
        print(f"Карта дилера: [{self.dealer.hand[0]}, ?]")

        # Ход игрока
        while self.player.sum < 21:
            answer = self.answer_hit()
            if answer == '1':
                self.player.take_card(self.deck.deal_card())
                print(f"\nВаши карты: {self.player.hand}, сумма: {self.player.sum}")
                if self.player.sum > 21:
                    print("Перебор! Вы проиграли.")
                    statistics_msg = f"Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
                    self.statistic_log.append(statistics_msg)
                    self.save()
                    return
            elif answer == '0':
                break
            elif answer == 'стоп':
                print("Игра прервана.")
                statistics_msg = f"Игра прервана. Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
                self.statistic_log.append(statistics_msg)
                self.save()
                return
            else:
                print("Неверный ввод. Введите 1, 0 или 'стоп'")

        if self.player.sum <= 21:
            if self.has_blackjack(self.dealer.hand):
                print(f"\nУ дилера Blackjack! {self.dealer.hand}")
                print("Дилер побеждает!")
                statistics_msg = f"Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
                self.statistic_log.append(statistics_msg)
                self.save()
                return
            else:
                self.dealer.play_dealer(self.deck)
                print(f"\nКарты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}")

        # Добавление записи в лог после завершения игры
        statistics_msg = f"Ваши карты: {self.player.hand}, сумма: {self.player.sum} Карты дилера: {self.dealer.hand}, сумма: {self.dealer.sum}"
        self.statistic_log.append(statistics_msg)
        self.determine_winner()

    def determine_winner(self):
        print("\n=== Результат ===")
        print(f"Ваши очки: {self.player.sum}")
        print(f"Очки дилера: {self.dealer.sum}")

        player_bj = self.has_blackjack(self.player.hand)
        dealer_bj = self.has_blackjack(self.dealer.hand)

        if player_bj and dealer_bj:
            print("Оба имеют Blackjack! Ничья!")
        elif player_bj:
            print("У вас Blackjack! Вы побеждаете!")
        elif dealer_bj:
            print("У дилера Blackjack! Дилер побеждает!")
        elif self.player.sum > 21:
            print("Вы перебрали! Дилер побеждает.")
        elif self.dealer.sum > 21:
            print("Дилер перебрал! Вы побеждаете!")
        elif self.player.sum > self.dealer.sum:
            print("Вы побеждаете!")
        elif self.player.sum < self.dealer.sum:
            print("Дилер побеждает.")
        else:
            print("Ничья!")

        self.save()  # Сохранение лога после определения победителя

#создаем экземпляр класса
session = GameSession()
#запускаем игру
session.start_session()



