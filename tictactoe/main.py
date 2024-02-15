import numpy as np
from typing import Optional


def create_grid(dimension: int) -> np.ndarray:
    grid = np.arange(1, dimension * dimension + 1).reshape(dimension, dimension)
    return grid


def check_winner(grid: np.ndarray) -> Optional[str]:
    # Check rows and columns for a winner
    for i in grid.shape[0]:
        if np.all(grid[i, :] == "X") or np.all(grid[:, i] == "X"):
            return "X wins!"
        elif np.all(grid[i, :] == "O") or np.all(grid[:, i] == "O"):
            return "O wins!"

    # Check diagonals for a winner
    if np.all(np.diag(grid) == "X") or np.all(np.diag(np.fliplr(grid)) == "X"):
        return 'X wins!'
    elif np.all(np.diag(grid) == "O") or np.all(np.diag(np.fliplr(grid)) == "O"):
        return "O wins!"

    # Check for a tie (no numbers left, meaning all cells are filled with 'X' or 'O')
    elif not np.any(grid.flatten().astype(str).isdigit()):
        return "Tie, no one wins :("

    # No winner yet
    return None