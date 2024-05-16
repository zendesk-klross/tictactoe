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

if __name__ == '__main__':
    app.run(debug=True)