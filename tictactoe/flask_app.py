from flask import Flask, render_template, request, redirect, url_for, session
from tictactoe import TicTacToe
from board import Board
from player import Player
from iohandler import IOHandler
from errors import InvalidMoveError
from constants import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed to use sessions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        player1_type = request.form['player1_type']
        player2_type = request.form['player2_type']
        board_size = int(request.form['board_size'])

        player1 = Player(name='Player 1', token='X', human=player1_type == 'human')
        player2 = Player(name= 'Player 2', token='O', human=player2_type == 'human')
        board = Board(col=board_size, row=board_size)
        game = TicTacToe(board, player1, player2)

        session['game_data'] = game.to_dict()
        return redirect(url_for('play'))
    
    return render_template('setup.html')


if __name__ == '__main__':
    app.run(debug=True)