import numpy as np
from constants import *

def board(row, col):
 board = np.array([str(i) for i in range(1, col*row + 1)]).reshape(col, row)
 return board

def play(board, game_status):
    print("TicTacToe <3")
    print(board)
    while game_status:
       move = input("Your move: ")
       move_position = np.where(board == move)
       board[move_position] = "X"
       print ("Moved to {}".format(move_position))
       print ("=============================")
       print(board)


game_board = board(BOARD_SIZE_ROW, BOARD_SIZE_COL)
play(game_board, GAME_ON)
