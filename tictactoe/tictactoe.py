import numpy as np
from board import Board
from player import Player

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
            print(self.board.__str__())
            end_game = self.board.check_winner()
            if end_game:
                print(end_game)
                self.is_played = False
            
            else:
                print("Turn: {}".format(current_player.name))
                move = input("Your move: ")
                move_position = np.where(self.board.grid == move)
                self.board.make_move(move_position, current_player.token)
                self.turn = 0 if self.turn else 1
                print ("Moved to {}".format(move_position))
                print ("=============================")

board = Board()
player1 = Player("X", "Player1")
player2 = Player("O", "Player2")
game = TicTacToe(board, player1, player2)
game.play()

