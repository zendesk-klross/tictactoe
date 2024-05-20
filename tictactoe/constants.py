# MAIN GAME LOOP
STARTUP_OPTS = ["Play",
                "Customize board size",
                "Select game mode",
                "Exit"]

BOARD_SIZE_OPTS = ["3x3",
                   "5x5",
                   "7x7",
                   "10x10",
                   "Custom"]

GAME_MODE_OPTS = ["Player vs Player",
                  "Player vs Computer",
                  "Computer vs Computer"]

# BEST MOVE SEARCH
EPSILON = 1e-6  # to avoid division by zero, small enough to not affect calculations
C_PARAM = 0.1  # exploration/exploitation balance constant
