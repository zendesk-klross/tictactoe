import numpy as np
from board import Board
from player import Player
import random

class TicTacToe:

    def __init__(self, board:Board, player1:Player, player2:Player, turn:int=0):
        self.is_played = True
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = turn

    def play(self):
        print("TicTacToe <3")
        print(self.board.__repr__())
        while self.is_played:
            current_player = self.player2 if self.turn else self.player1
            print(self.board)
            end_game = self.board.check_winner()
            if end_game:
                print(end_game)
                self.is_played = False
            
            else:
                while True:
                    print("Turn: {}".format(current_player.name))
                    available_cells = self.board.available_cells()
                    print(available_cells)
                    if current_player.human:
                        move = input("Your move: ")
                    else:
                        move = random.choice(available_cells)

                    make_move = self.board.make_move(move, current_player.token)
                    if make_move:
                        self.turn = 0 if self.turn else 1
                        print("Moved to {}".format(move))
                        print("=============================")
                        break
                    else:
                        print("Please make a different move.")

board = Board()
player1 = Player("X", "Player1")
player2 = Player("O", "Player2", human=False)
game = TicTacToe(board, player1, player2)
game.play()

