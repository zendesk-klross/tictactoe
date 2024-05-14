import numpy as np
from typing import Optional
from .errors import InvalidMoveError


class Board:
    def __init__(self, col:int, row:int):
        self.col = col
        self.row = row
        self.grid = np.array([str(i) for i in range(1, self.col*self.row + 1)]).reshape(self.col, self.row)

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __getitem__(self, key):
        return self.grid[key]

    def available_cells(self):
        available_cells = []
        for row in self.grid:
            for elem in row:
                if str(elem).isdigit():
                    available_cells.append(elem)
        return available_cells
    
    def make_move(self, move, token):
        if move.isdigit() and 1 <= int(move) <= self.row * self.col + 1:
            position = np.where(self.grid == move)
            if len(position[0]) > 0:
                self.grid[position] = token
                return self
            else:
                raise InvalidMoveError('That cell is already occupied.')
        else:
            raise InvalidMoveError('Please choose a valid number.')
        return False

    def check_winner(self, token1, token2) -> Optional[str]:
        # Check rows and columns for a winner
        for i in range(min(self.grid.shape)):
            if np.all(self[i, :] == token1) or np.all(self.grid[:, i] == token1):
                return token1
            elif np.all(self.grid[i, :] == token2) or np.all(self.grid[:, i] == token2):
                return token2

        # Check diagonals for a winner
        if np.all(np.diag(self.grid) == token1) or np.all(np.diag(np.fliplr(self.grid)) == token1):
            return token1
        if np.all(np.diag(self.grid) == token2) or np.all(np.diag(np.fliplr(self.grid)) == token2):
            return token2

        # Check for a tie (no numbers left, meaning all cells are filled)
        if not np.any([cell.isdigit() for cell in self.grid.flatten()]):
            return -1

        # No winner yet
        return None

