import pytest
import numpy as np
from tictactoe.board import Board
from tictactoe.best_move_search import BestMoveSearch
from tictactoe.player import Player
from tictactoe.tictactoe import TicTacToe


class TestBestMoveSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.board = Board(3, 3)
        self.player1 = Player('X', 'Player1')
        self.player2 = Player('X', 'Player2')
        self.game = TicTacToe(self.board, self.player1, self.player2)
        self.best_move_search = BestMoveSearch(self.game)

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

    def test_expand(self):
        # Initial list of children is empty
        assert len(self.best_move_search.children) == 0

        child_node = self.best_move_search.expand()

        # After expand, there is 1 child, whose parent is previous move
        # and action is previous action
        assert len(self.best_move_search.children) == 1
        assert child_node.parent == self.best_move_search
        assert child_node.parent_action == "9"

        # Check if the untried actions have been updated
        assert "9" not in self.best_move_search._untried_actions
        for i in range(1, 9):
            assert str(i) in self.best_move_search._untried_actions

    def test_is_expanded(self):
        assert not self.best_move_search.is_expanded()

        self.best_move_search._untried_actions = []
        assert self.best_move_search.is_expanded()

    def test_simulate_playthrough(self):
        self.game.board.grid = np.array([['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', 'X', 'O']])
        assert self.best_move_search.simulate_playthrough() is None

        self.board.grid = np.array([['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', '8', 'X']])
        assert self.best_move_search.simulate_playthrough() == 'X'

        self.board.grid = np.array([['X', 'O', '3'],
                                    ['X', 'O', '6'],
                                    ['O', 'O', 'X']])
        assert self.best_move_search.simulate_playthrough() == 'O'

        self.board.grid = np.array([['X', 'O', 'X'],
                                    ['X', 'O', 'X'],
                                    ['O', 'X', 'O']])

        assert self.best_move_search.simulate_playthrough() is None



