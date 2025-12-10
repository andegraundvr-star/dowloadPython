#Крестики-нолики

import random

class Field:
    def __init__(self):
        self.our_field = ['1','2','3','4','5','6','7','8','9']
    #создаем функцию вызова занятия поля и удаления его общего списка клеток
    def deal_cell(self, cell):
        return cell in self.our_field
    #создаем функцию для удаления занятого поля из списка
    def occupy_cell(self, cell):
        if cell in self.our_field:
            self.our_field.remove(cell)
            return True
        return False
#создаем класс игрока
class Player:
    def __init__(self):
        self.hand = []
    #набор занятых клеток в список полей игрока
    def occupy_cell(self, cell):
        self.hand.append(cell)

#создаем класс компьютера
class Computer:
    def __init__(self):
        self.hand = []
    #набор занятых клеток в список полей компьютера
    def occupy_cell(self, cell):
        self.hand.append(cell)

#создаем класс игры
class Game:
    #инициируем поле и игроков
    def __init__(self):
        self.field = Field()
        self.computer = Computer()
        self.player = Player()
        self.winning_combinations = [
            {'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'},
            {'1', '4', '7'}, {'2', '5', '8'}, {'3', '6', '9'},
            {'1', '5', '9'}, {'3', '5', '7'}
        ]
    #создаем метод проверки на выигрыш
    def check_win(self, hand):
        hand_set = set(hand)
        for combo in self.winning_combinations:
            if combo.issubset(hand_set):
                return True
        return False
    def start_game(self):
        print("Добро пожаловать в игру Крестики - нолики!")
        while True: #главный цикл
            #ход игрока
            while True:
                answer = input("\nна какую клетку ставим крестик? (от 1 до 9): ")
                #проверка на занятость клетки и выигрышную комбинацию
                if not self.field.deal_cell(answer):
                    print(f"Клетка {answer} занята или не существует, выберите другую")
                    continue
                #занимаем клетку
                if self.field.occupy_cell(answer):
                    self.player.occupy_cell(answer)
                    break
            #проверка победы игрока
            if self.check_win(self.player.hand):
                print("Вы выиграли!")
                return
            #проверка ничьи
            if not self.field.our_field:
                print("Ничья!")
                return

            #ход компьютера
            comp_answer = random.choice(self.field.our_field)
            self.field.occupy_cell(comp_answer)
            self.computer.occupy_cell(comp_answer)
            print(f"Компьютер выбрал клетку {comp_answer}")
            #проверка на выигрышную комбинацию
            #проверка победы компьютера
            if self.check_win(self.computer.hand):
                print("Компьютер победил!")
                return
            #проверка ничьи
            if not self.field.our_field:
                print("Ничья!")
                return
#создаем экземпляры класса
game = Game()
#запускаем игру
game.start_game()

