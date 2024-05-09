from .board import Board
import numpy as np
from collections import defaultdict


class BestMoveSearch:
    def __init__(self, board=Board, parent=None, parent_action=None):
        self.board = board
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
        self._untried_actions = self.board.available_cells()
        return self._untried_actions

    def is_terminal_node(self):
        return self.board.is_game_over()

    def wins_losses_difference(self):
        wins = self._results[1]
        losses = self._results[-1]
        return wins-losses

    def times_visited(self):
        return self._number_of_visits




