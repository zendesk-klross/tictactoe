from flask import Flask, render_template, request, redirect, url_for, session
from tictactoe import TicTacToe
from board import Board
from player import Player
from iohandler import IOHandler
from errors import InvalidMoveError
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed to use sessions


@app.route('/')
def index():
    with open('assets/hero_text.txt', 'r') as file:
        hero_text = file.read()
    return render_template('index.html', hero_text=hero_text)


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        board_size = int(request.form['board_size'])

        player1_name = request.form['player1_name']
        player2_name = request.form['player2_name']

        player1_type = request.form['player1_type']
        player2_type = request.form['player2_type']

        # No computer + computer combination allowed
        if player1_type == 'computer' and player2_type == 'computer':
            error_message = "Computer vs. Computer games are not allowed." # todo: fix, message not printed
            return render_template('setup.html', error=error_message) 

        player1 = Player(name=player1_name, token='X', human=player1_type == 'human')
        player2 = Player(name=player2_name, token='O', human=player2_type == 'human')
        board = Board(col=board_size, row=board_size)
        game = TicTacToe(board, player1, player2)

        session['game_data'] = game.to_dict()
        return redirect(url_for('next_move'))
    
    return render_template('setup.html')


@app.route('/next_move')
def next_move():
    game_data = session.get('game_data')
    if not game_data:
        return redirect(url_for('setup'))
    game = TicTacToe.from_dict(game_data, IOHandler())
    current_player = game.player2 if game.turn else game.player1

    if current_player.human:
        return redirect(url_for('human_move'))
    else:
        return redirect(url_for('computer_move'))


@app.route('/human_move', methods=['GET', 'POST'])
def human_move():
    game_data = session.get('game_data')
    if not game_data:
        return redirect(url_for('setup'))
    game = TicTacToe.from_dict(game_data, IOHandler())

    if request.method == 'POST':
        row = request.form.get('move_row')
        col = request.form.get('move_col')
        if row is not None and col is not None:
            move = str(int(row) * game.board.col + int(col) + 1)
            try:
                game.board.make_move(move, game.player1.token if game.turn == 0 else game.player2.token)
                game.turn = 1 - game.turn
                session['game_data'] = game.to_dict()
                winner = game.get_winner()
                if winner or not game.board.available_cells():
                    # Game over, display the result
                    return redirect(url_for('game_over', winner=winner.name if winner else "Draw"))
                else:
                    # Game continues, go to the next move
                    return redirect(url_for('next_move'))
            except InvalidMoveError as e:
                # Handle invalid move
                pass

    return render_template('play.html', game=game)

@app.route('/computer_move')
def computer_move():
    game_data = session.get('game_data')
    if not game_data:
        return redirect(url_for('setup'))
    game = TicTacToe.from_dict(game_data, IOHandler())

    available_cells = game.board.available_cells()
    move = random.choice(available_cells)
    game.board.make_move(move, game.player1.token if game.turn == 0 else game.player2.token)
    game.turn = 1 - game.turn
    session['game_data'] = game.to_dict()

    winner = game.get_winner()
    if winner or not game.board.available_cells():
        # Game over, display the result
        return redirect(url_for('game_over', winner=winner.name if winner else "Draw"))
    else:
        # Game continues, go to the next move
        return redirect(url_for('next_move'))

@app.route('/game_over')
def game_over():
    winner = request.args.get('winner', 'Nobody')  # Default to 'Nobody' if no winner
    message = f"{winner} wins!" if winner != "Draw" else "The game is a draw!"
    # Clear the game data from the session
    session.pop('game_data', None)
    return render_template('game_over.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)


# TODO
# Add computer player logic to play function
# Refactor play function - avoid code duplication from tictactoe class

