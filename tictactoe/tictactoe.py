import sys

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
            end_game = self.board.check_winner(self.player1.token, self.player2.token)
            if end_game:
                self.io.pretty_print_grid(self.board.grid)
                self.io.output(end_game)
                self.is_played = False
            else:
                while True:
                    error = None
                    self.io.clear_screen()
                    self.io.output(error) if error else None
                    self.io.output("Turn: {}".format(current_player.name))
                    self.io.pretty_print_grid(self.board.grid)
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

