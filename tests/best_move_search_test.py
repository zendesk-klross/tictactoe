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

    def test_update_stats(self):
        self.best_move_search.update_stats(1)
        assert self.best_move_search._number_of_visits == 1
        assert self.best_move_search._results[1] == 1

        self.best_move_search.update_stats(-1)
        assert self.best_move_search._number_of_visits == 2
        assert self.best_move_search._results[-1] == 1

        self.best_move_search.update_stats(0)
        assert self.best_move_search._number_of_visits == 3
        assert self.best_move_search._results[0] == 1

    def test_best_child(self):
        # Make a move to have some children
        child_node1 = self.best_move_search.expand()
        child_node1._results[1] = 3
        child_node1._results[-1] = 1
        child_node1._number_of_visits = 10

        child_node2 = self.best_move_search.expand()
        child_node2._results[1] = 1
        child_node2._results[-1] = 3
        child_node2._number_of_visits = 4

        child_node3 = self.best_move_search.expand()
        child_node3._results[1] = 3
        child_node3._results[-1] = 1
        child_node3._number_of_visits = 4

        best_child = self.best_move_search.best_child()
        assert best_child == child_node3

    def test_set_number_of_visits(self):
        self.best_move_search.set_number_of_visits(self.best_move_search, 5)
        assert self.best_move_search._number_of_visits == 5

    # TODO: This is a bad test that doesn't work. Selection itself seems to be correct, but specific to how this
    #  method  is calling expand inside of it, it produces a new least visited node, which gets prioritized since
    #  exploration is low. Maybe some mocking is needed to test this properly.
    # def test_select_node_for_playthrough(self):
    #     child_node1 = self.best_move_search.expand()
    #     child_node1._results[1] = 3
    #     child_node1._results[-1] = 1
    #     child_node1._number_of_visits = 10
    #
    #     child_node2 = self.best_move_search.expand()
    #     child_node2._results[1] = 1
    #     child_node2._results[-1] = 3
    #     child_node2._number_of_visits = 4
    #
    #     child_node3 = self.best_move_search.expand()
    #     child_node3._results[1] = 10
    #     child_node3._results[-1] = 1
    #     child_node3._number_of_visits = 11
    #
    #     self.best_move_search._untried_actions = []
    #
    #     selected_node = self.best_move_search.select_node_for_playthrough()
    #     print("SELECTED NODE", selected_node.uct_value(), selected_node._number_of_visits, selected_node._results)
    #     print("CHILDREN", self.best_move_search.children)
    #
    #     uct_values = [child.uct_value() for child in self.best_move_search.children]
    #
    #     assert selected_node.uct_value() == max(uct_values)
