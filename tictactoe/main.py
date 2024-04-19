from tictactoe import TicTacToe
from board import Board
from player import Player
from iohandler import IOHandler
from constants import *
import os

def startup(io, board, player1, player2, game):
    io.clear_screen()
    io.output_from_file("tictactoe/assets/hero_text.txt")

    player_choice = io.input_options("Press space > ", STARTUP_OPTS).strip()
    if player_choice == STARTUP_OPTS[3]:
        io.output("\nThanks for playing <3")
        game.exit()
    elif player_choice == STARTUP_OPTS[0]:
        io.output("\nTo make a move, type the number of the cell you want to place your token in.\n")
        game.play()


board = Board()
player1 = Player("X", "Player1")
player2 = Player("O", "Player2", human=False)
io = IOHandler()
game = TicTacToe(board, player1, player2, io)

startup(io, board, player1, player2, game)

# TODO:
# 1. Make computer an instance of the player class,take the logic out of the main game
# 2. Customize the board size
# 3. Select game mode

