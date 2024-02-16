import numpy as np
from board import Board
import player

class TicTacToe:

    def __init__(self, board:Board):
        self.is_played = True
        self.board = board

    def play(self):
        print("TicTacToe <3")
        print(self.board)
        while True:
            move = input("Your move: ")
            move_position = np.where(board == move)
            self.board[move_position] = "X"
            print ("Moved to {}".format(move_position))
            print ("=============================")
            print(self.board)




board = Board()
game = TicTacToe(board)
game.play()