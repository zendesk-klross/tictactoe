import pytest
import numpy as np
from tictactoe.board import Board


@pytest.fixture
def board():
    return Board()


def test_row_winner(board):
    board.grid[0, :] = 'X'  # Set the first row to 'X'
    assert board.check_winner() == 'X wins!'


def test_column_winner(board):
    board.grid[:, 0] = 'O'  # Set the first column to 'O'
    assert board.check_winner() == 'O wins!'


def test_diagonal_winner(board):
    #breakpoint()
    np.fill_diagonal(board.grid, 'X')  # Set the main diagonal to 'X'
    assert board.check_winner() == 'X wins!'


def test_tie(board):
    board.grid = np.array([['X', 'O', 'X'],
                            ['X', 'X', 'O'],
                            ['O', 'X', 'O']])
    assert board.check_winner() == 'Tie, no one wins :('


def test_no_winner(board):
    assert board.check_winner() is None