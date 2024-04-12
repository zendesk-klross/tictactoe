import pytest
from board import Board


@pytest.fixture
def board():
    return Board()


def test_make_valid_move(board):
    move = '1'
    token = 'X'
    assert board.make_move(move, token) == True
    assert board.grid[0, 0] == token


def test_make_invalid_move(board):
    move = '1'
    token = 'X'
    board.make_move(move, token)

    repeat_move = '1'
    assert board.make_move(repeat_move, token) == False

    out_of_range_move = '10'
    assert board.make_move(out_of_range_move, token) == False

    non_digit_move = 'a'
    assert board.make_move(non_digit_move, token) == False