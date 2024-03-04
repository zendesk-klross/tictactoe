import numpy as np
from typing import Optional


class Board:

    # @TODO: Write a setter for the board cell values
    def __init__(self, col:int=3, row:int=3):
        self.col = col
        self.row = row
        self.board = np.array([str(i) for i in range(1, self.col*self.row + 1)]).reshape(self.col, self.row)
    def __repr__(self):
        return str(self.board)

    def make_move(self, position, move):
        self.board[position] = move

    def check_winner(self) -> Optional[str]:
        # Check rows and columns for a winner
        for i in self.shape[0]:
            if np.all(self[i, :] == "X") or np.all(self[:, i] == "X"):
                return "X wins!"
            elif np.all(self[i, :] == "O") or np.all(self[:, i] == "O"):
                return "O wins!"

        # Check diagonals for a winner
        if np.all(np.diag(self) == "X") or np.all(np.diag(np.fliplr(self)) == "X"):
            return 'X wins!'
        elif np.all(np.diag(self) == "O") or np.all(np.diag(np.fliplr(self)) == "O"):
            return "O wins!"

        # Check for a tie (no numbers left, meaning all cells are filled with 'X' or 'O')
        # @TODO: We need to fix this pls
        # elif not np.any(self.flatten().astype(str).isdigit()):
        #     return "Tie, no one wins :("

        # No winner yet
        return None