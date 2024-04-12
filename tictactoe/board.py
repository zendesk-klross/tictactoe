import numpy as np
from typing import Optional


class Board:
    def __init__(self, col:int=3, row:int=3):
        self.col = col
        self.row = row
        self.grid = np.array([str(i) for i in range(1, self.col*self.row + 1)]).reshape(self.col, self.row)

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __getitem__(self, key):
        return self.grid[key]

    def __repr__(self):
        return str(self.grid)

    def __str__(self):
        pretty_grid = np.where((self.grid != 'X') & (self.grid != 'O'), ' ', self.grid)
        return '\n'.join(' | '.join(row) for row in pretty_grid)
    
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
                return True
            else:
                print('That cell is already occupied.')
        else:
            print('Please choose a valid number.')
        return False

    def check_winner(self) -> Optional[str]:
        # Check rows and columns for a winner
        for i in range(self.grid.shape[0]):
            if np.all(self[i, :] == "X") or np.all(self.grid[:, i] == "X"):
                return "X wins!"
            elif np.all(self.grid[i, :] == "O") or np.all(self.grid[:, i] == "O"):
                return "O wins!"

        # Check diagonals for a winner
        if np.all(np.diag(self.grid) == "X") or np.all(np.diag(np.fliplr(self.grid)) == "X"):
            return 'X wins!'
        if np.all(np.diag(self.grid) == "O") or np.all(np.diag(np.fliplr(self.grid)) == "O"):
            return "O wins!"

        # Check for a tie (no numbers left, meaning all cells are filled with 'X' or 'O')
        if not np.any([cell.isdigit() for cell in self.grid.flatten()]):
            return "Tie, no one wins :("

        # No winner yet
        return None
