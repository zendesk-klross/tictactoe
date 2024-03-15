import numpy as np
from board import Board
from player import Player
from iohandler import IOHandler

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
                self.io.output("Turn: {}".format(current_player.name))
                move = self.io.input("Your move: ")
                move_position = np.where(self.board.grid == move)
                self.board.make_move(move_position, current_player.token)
                self.turn = 0 if self.turn else 1
                self.io.output ("=============================")

board = Board()
player1 = Player("X", "Player1")
player2 = Player("O", "Player2")
io = IOHandler()
game = TicTacToe(board, player1, player2, io)
game.play()

