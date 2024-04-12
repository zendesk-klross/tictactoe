import numpy as np
from board import Board
from player import Player
from iohandler import IOHandler
import random


class TicTacToe:

    def __init__(self, board:Board, player1:Player, player2:Player, io:IOHandler=IOHandler(), turn:int=0):
        self.is_played = True
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.io = io
        self.turn = turn

    def play(self):
        self.io.output("TicTacToe <3")
        self.io.output(self.board.__repr__())
        while self.is_played:
            current_player = self.player2 if self.turn else self.player1
            self.io.output(self.board.__str__())
            end_game = self.board.check_winner()
            if end_game:
                self.io.output(end_game)
                self.is_played = False
            
            else:
                while True:
                    self.io.output("Turn: {}".format(current_player.name))
                    available_cells = self.board.available_cells()
                    self.io.output(available_cells)
                    if current_player.human:
                        move = self.io.input("Your move: ")
                    else:
                        move = random.choice(available_cells)

                    make_move = self.board.make_move(move, current_player.token)
                    if make_move:
                        self.turn = 0 if self.turn else 1
                        self.io.output("Moved to {}".format(move))
                        self.io.output("=============================")
                        break
                    else:
                        self.io.output("Please make a different move.")

board = Board()
player1 = Player("X", "Player1")
player2 = Player("O", "Player2", human=False)
io = IOHandler()
game = TicTacToe(board, player1, player2, io)

game.play()

