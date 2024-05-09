import pytest
import numpy as np
from tictactoe.board import Board
from tictactoe.best_move_search import BestMoveSearch


class TestBestMoveSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.board = Board(3, 3)
        self.best_move_search = BestMoveSearch(self.board)

    def test_untried_actions(self):
        expected_untried_actions = [str(i) for i in range(1, 10)]
        assert self.best_move_search.untried_actions() == expected_untried_actions
        # Make a move and check the untried actions again
        self.board.make_move("1", "X")
        expected_untried_actions.remove("1")
        assert self.best_move_search.untried_actions() == expected_untried_actions

    def test_is_terminal_node(self):
        assert not self.best_move_search.is_terminal_node()

        self.board.grid = np.array([['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', 'X', 'O']])
        assert self.best_move_search.is_terminal_node()

    def test_wins_losses_difference(self):
        assert self.best_move_search.wins_losses_difference() == 0

        self.best_move_search._results[1] = 3
        self.best_move_search._results[-1] = 1
        assert self.best_move_search.wins_losses_difference() == 2

    def test_times_visited(self):
        assert self.best_move_search.times_visited() == 0

        self.best_move_search._number_of_visits = 5
        assert self.best_move_search.times_visited() == 5
