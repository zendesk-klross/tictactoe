import numpy as np
import random
from board import Board
from player import Player
from iohandler import IOHandler
from errors import *

class TicTacToe:

    def __init__(self, board:Board, player1:Player, player2:Player, io:IOHandler=IOHandler(), turn:int=0):
        self.is_played = True
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.io = io
        self.turn = turn

    def play(self):
        while self.is_played:
            current_player = self.player2 if self.turn else self.player1
            winner = self.get_winner()
            if winner:
                self.io.clear_screen()
                self.io.pretty_print_grid(self.board.grid, self.player1.token, self.player2.token)
                if winner == -1:
                    self.io.output("It's a tie!🤝")
                elif winner.name == "Player":
                    self.io.output(f"You win!🎉")
                else:
                    self.io.output(f"{winner.name} wins!🎉")
                self.is_played = False
            else:
                while True:
                    error = None

                    self.io.clear_screen()
                    self.io.output(error) if error else None
                    self.io.output("Turn: {}".format(current_player.name))
                    self.io.output("\nTo make a move, type the number of the cell you want to place your token in.\n")
                    self.io.pretty_print_grid(self.board.grid, self.player1.token, self.player2.token)

                    available_cells = self.board.available_cells()
                    if current_player.human:
                        move = self.io.input("Your move")
                    else:
                        self.io.progress_bar("Thinking ")
                        move = random.choice(available_cells)
                    try:
                        make_move = self.board.make_move(move, current_player.token)
                        if make_move:
                            self.turn = 0 if self.turn else 1
                            break
                    except InvalidMoveError as e:
                        error = str(e)

    def get_winner(self):
        winning_token = self.board.check_winner(self.player1.token, self.player2.token)
        if winning_token == self.player1.token:
            return self.player1
        elif winning_token == self.player2.token:
            return self.player2
        elif winning_token == -1:
            return -1
        else:
            return None