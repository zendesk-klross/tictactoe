import pytest
import numpy as np
import tictactoe.board
    

@pytest.fixture
def board():
    return tictactoe.board.Board()


def test_initialization(board):
    expected_grid = np.array([[str(i) for i in range(1, 10)]]).reshape(3, 3)
    assert board.row == 3
    assert board.col == 3
    assert np.array_equal(board.grid, expected_grid)


def test_repr_(board):
    expected_repr = "[['1' '2' '3']\n ['4' '5' '6']\n ['7' '8' '9']]"
    assert repr(board) == expected_repr


def test_str_method_with_moves(board):
    board.grid[0][0] = 'X'
    board.grid[1][1] = 'O'
    expected_str = 'X |   |  \n  | O |  \n  |   |  '
    assert str(board) == expected_str


def test_make_move(board):
    board.make_move((0, 0), 'X')
    assert board.grid[0][0] == 'X'


def test_row_winner(board):
    board.grid[0, :] = 'X'  # Set the first row to 'X'
    assert board.check_winner() == 'X wins!'


def test_column_winner(board):
    board.grid[:, 0] = 'O'  # Set the first column to 'O'
    assert board.check_winner() == 'O wins!'


def test_diagonal_winner(board):
    # breakpoint()
    np.fill_diagonal(board.grid, 'X')  # Set the main diagonal to 'X'
    assert board.check_winner() == 'X wins!'


def test_tie(board):
    board.grid = np.array([['X', 'O', 'X'],
                           ['X', 'X', 'O'],
                           ['O', 'X', 'O']])
    assert board.check_winner() == 'Tie, no one wins :('


def test_no_winner(board):
    assert board.check_winner() is None
