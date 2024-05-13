import pytest
import numpy as np
import tictactoe.board
    

@pytest.fixture
def board():
    return tictactoe.board.Board(3, 3)


def test_initialization(board):
    expected_grid = np.array([[str(i) for i in range(1, 10)]]).reshape(3, 3)
    assert board.row == 3
    assert board.col == 3
    assert np.array_equal(board.grid, expected_grid)


def test_make_move(board):
    board.make_move("1", 'X')
    assert board.grid[0][0] == 'X'


def test_row_winner(board):
    board.grid[0, :] = 'X'  # Set the first row to 'X'
    assert board.check_winner('X', '0') == 'X'


def test_column_winner(board):
    board.grid[:, 0] = 'O'  # Set the first column to 'O'
    assert board.check_winner('X', 'O') == 'O'


def test_diagonal_winner(board):
    # breakpoint()
    np.fill_diagonal(board.grid, 'X')  # Set the main diagonal to 'X'
    assert board.check_winner('X', 'O') == 'X'


def test_tie(board):
    board.grid = np.array([['X', 'O', 'X'],
                           ['X', 'X', 'O'],
                           ['O', 'X', 'O']])
    assert board.check_winner('X', 'O') is None

    