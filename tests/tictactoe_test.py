from unittest import mock

import pytest

from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.tictactoe import TicTacToe


@pytest.fixture
def board():
    return Board()


@pytest.fixture
def player1():
    return Player('X', 'Player1')


@pytest.fixture
def player2():
    return Player('O', 'Player2')


@pytest.fixture
def game(board, player1, player2):
    return TicTacToe(board, player1, player2)


def test_tictactoe_initialization(game, board, player1, player2):
    assert game.board == board
    assert game.player1 == player1
    assert game.player2 == player2
    assert game.turn == 0
    assert game.is_played