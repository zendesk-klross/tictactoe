from .board import Board
from .tictactoe import TicTacToe
from .constants import EPSILON, C_PARAM
import numpy as np
from collections import defaultdict


class BestMoveSearch:
    def __init__(self, game=TicTacToe, parent=None, parent_action=None):
        self.game = game
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = self.untried_actions()
        return

    def untried_actions(self):
        self._untried_actions = self.game.board.available_cells()
        return self._untried_actions

    def is_terminal_node(self):
        return self.game.is_game_over()

    def wins_losses_difference(self):
        wins = self._results[1]
        losses = self._results[-1]
        return wins-losses

    def times_visited(self):
        return self._number_of_visits

    # Populate list of child nodes with all possible moves
    def expand(self):
        action = self._untried_actions.pop()
        original_game_state = self.game.board.grid.copy()

        self.game.board.make_move(action, self.game.current_player.token)

        child_node = BestMoveSearch(self.game,
                                    parent=self,
                                    parent_action=action)
        self._number_of_visits += 1
        child_node._number_of_visits += 1
        self.children.append(child_node)
        self.game.board.grid = original_game_state
        return child_node

    def is_expanded(self):
        return len(self._untried_actions) == 0

    # this is the "rollout" of the game. I am calling it so
    # to better understand what I am doing
    def simulate_playthrough(self):
        current_board = self.game.board
        while not self.game.is_game_over():
            available_cells = current_board.available_cells()
            move = np.random.choice(available_cells)
            current_board = current_board.make_move(move, self.game.current_player.token)
        return current_board.check_winner("X", "O")

    # Backpropagate the result of the game to the root node
    def update_stats(self, result):
        self._number_of_visits += 1
        self._results[result] += 1
        if self.parent:
            self.parent.update_stats(result)
        return

    # Upper Confidence Bound for a node
    def uct_value(self):
        exploitation = self.wins_losses_difference() / (self.times_visited() + EPSILON)
        exploration = C_PARAM * np.sqrt((2 * np.log(self.times_visited() + EPSILON) / (self.times_visited() + EPSILON)))
        return exploitation + exploration

    def best_child(self):
        choices_weights = []
        for child in self.children:
            # avoiding division by zero
            if self.times_visited() + EPSILON < 1 or child.times_visited() + EPSILON < 1:
                choices_weights.append(0)
            else:
                choices_weights.append(child.uct_value())

        return self.children[np.argmax(choices_weights)]

    def select_node_for_playthrough(self):
        current_node = self
        while not current_node.is_terminal_node():
            if not current_node.is_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node
