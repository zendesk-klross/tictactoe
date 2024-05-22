import sys

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


@app.route('/play', methods=['GET', 'POST'])
def play():
    # Retrieve the serialized game data from the session
    game_data = session.get('game_data')
    if not game_data:
        return redirect(url_for('setup'))

    # Reconstruct the TicTacToe object from the game data
    game = TicTacToe.from_dict(game_data, IOHandler())
    message = None
    error = None

    if request.method == 'POST':
        row = request.form.get('move_row')
        col = request.form.get('move_col')
        if row is not None and col is not None:
            row, col = int(row), int(col)
            move = str(row * game.board.col + col + 1)
            current_player = game.player2 if game.turn else game.player1

        if current_player.human:
            if move and move.isdigit() and move in game.board.available_cells():
                try:
                    game.board.make_move(move, current_player.token)
                    game.turn = 1 - game.turn  # Switch turns
                except InvalidMoveError as e:
                    error = str(e)
            else:
                error = "Invalid move! Please try again."
        else:
            # TODO
            pass

        winner = game.get_winner()
        if winner:
            message = f"{winner.name} wins!🎉"
            game.is_played = False
            # Clear the game data from the session as the game is over
            session.pop('game_data', None)
        elif not game.board.available_cells():
            message = "The game is a draw!"
            game.is_played = False
            # Clear the game data from the session as the game is over
            session.pop('game_data', None)

        # Game isn't over, save the updated state in the session
        if game.is_played:
            session['game_data'] = game.to_dict()
            
    return render_template('play.html', game=game, message=message, error=error)


if __name__ == '__main__':
    app.run(debug=True)


# TODO
# Add computer player logic to play function
# Refactor play function - avoid code duplication from tictactoe class
# Pretty board display
# Select cells instead of inputing a move

