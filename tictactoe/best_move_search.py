from .board import Board
from .constants import EPSILON, C_PARAM
import numpy as np
from collections import defaultdict


class BestMoveSearch:
    def __init__(self, board=Board, parent=None, parent_action=None, token1='X', token2='O', current_token='X', turn=0):
        self.board = board
        self._simulation_board = self.board.copy()
        self.token1 = token1
        self.token2 = token2
        self.turn = turn
        self.current_token = current_token
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
        self._untried_actions = self._simulation_board.available_cells()
        return self._untried_actions

    def is_terminal_node(self):
        return self.is_game_over()

    def wins_losses_difference(self):
        wins = self._results[1]
        losses = self._results[-1]
        return wins-losses

    def times_visited(self):
        return self._number_of_visits

    # Populate list of child nodes with all possible moves
    def expand(self):
        action = self._untried_actions.pop()
        new_simulation_board = self._simulation_board.copy()
        new_simulation_board.make_move(action, self.current_token)

        child_node = BestMoveSearch(new_simulation_board,
                                    parent=self,
                                    parent_action=action,
                                    token1=self.token1,
                                    token2=self.token2,
                                    current_token = self.token2 if self.current_token == self.token1 else self.token1,
                                    turn=1 if self.turn == 0 else 0)
        self._number_of_visits += 1
        child_node._number_of_visits += 1
        self.children.append(child_node)
        return child_node

    def is_expanded(self):
        return len(self._untried_actions) == 0

    # this is the "rollout" of the game. I am calling it so
    # to better understand what I am doing
    def simulate_playthrough(self):
        current_board = self._simulation_board
        current_token = self.current_token
        while not self.is_game_over():
            available_cells = current_board.available_cells()
            move = np.random.choice(available_cells)
            current_board.make_move(move, current_token)
            current_token = self.token2 if current_token == self.token1 else self.token1


        return current_board.check_winner(self.token1, self.token2)

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

    # Tree policy
    def select_node_for_playthrough(self):
        current_node = self
        while not current_node.is_terminal_node():
            if not current_node.is_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    def best_move(self):
        simulation_no = 1000

        for i in range(simulation_no):
            if self.is_game_over(): break
            node = self.select_node_for_playthrough()
            reward = node.simulate_playthrough()
            node.update_stats(reward)
            self.current_token = self.token2 if self.current_token == self.token1 else self.token1
            self.turn = 0 if self.turn else 1

        best_child = self.best_child()
        return str(best_child.parent_action)

    def is_game_over(self):
        winner = self._simulation_board.check_winner(self.token1, self.token2)
        if (winner or not self._simulation_board.available_cells()): return True
        else: return False


