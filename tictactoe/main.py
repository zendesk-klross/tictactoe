from tictactoe import TicTacToe
from board import Board
from player import Player
from iohandler import IOHandler
from constants import *
import os

def startup(io=IOHandler()):
    board_height = None
    board_width = None
    player1 = None
    player2 = None

    io.clear_screen()
    io.output_from_file("tictactoe/assets/hero_text.txt")

    while True:
        io.output("Player1 is {}".format(player1.name if player1 else "not set"))
        io.output("Player2 is {}".format(player2.name if player2 else "not set"))
        player_choice = io.input_options("Press space > ", STARTUP_OPTS).strip()

        # EXIT
        if player_choice == STARTUP_OPTS[3]:
            io.output("\nThanks for playing <3")
            break

        # SELECT BOARD SIZE
        elif player_choice == STARTUP_OPTS[1]:
            board_size = io.input_options("Select board size (press space): ", BOARD_SIZE_OPTS).strip()
            # Custom board size
            if board_size == BOARD_SIZE_OPTS[4]:
                board_width = io.input("Enter board width")
                board_height = io.input("Enter board height")
            else:
                board_width, board_height = board_size.split("x")
            # board = Board(int(board_width), int(board_height))
            io.output("\nBoard size set to {}x{}\n".format(board_width, board_height))
            continue

        # SELECT GAME MODE
        elif player_choice == STARTUP_OPTS[2]:
            game_mode = io.input_options("Select game mode: ", GAME_MODE_OPTS).strip()
            # Computer VS Computer
            if game_mode == GAME_MODE_OPTS[2]:
                player1 = Player("X", "Computer1", human=False)
                player2 = Player("O", "Computer2", human=False)
                continue
            # Player VS Computer
            elif game_mode == GAME_MODE_OPTS[1]:
                name = io.input("Enter your name")
                token = io.input("Select your token(X, 0)").strip().upper()

                if not token: token = "X"
                if not name: name = "Player"

                if token == "O":
                    player1 = Player("X", "Computer", human=False)
                    player2 = Player(token, name, human=True)
                else:
                    player1 = Player(token, name, human=True)
                    player2 = Player("O", "Computer", human=False)
            # Player VS Player
            elif game_mode == GAME_MODE_OPTS[0]:
                name1 = io.input("Enter Player1 name")
                token1 = io.input("Select Player1 token").strip().upper()
                name2 = io.input("Enter Player2 name")
                token2 = io.input("Select Player2 token").strip().upper()

                if not name1: name1 = "Player1"
                if not name2: name2 = "Player2"
                if not token1: token1 = "X"
                if not token2: token2 = "O"

                if token1 == "X":
                    player1 = Player(token1, name1, human=True)
                    player2 = Player(token2, name2, human=True)
                else:
                    player1 = Player(token2, name2, human=True)
                    player2 = Player(token1, name1, human=True)

            continue

        # START GAME
        elif player_choice == STARTUP_OPTS[0]:
            if not board_width or not board_height:
                board_width, board_height = 3, 3
            if not player1:
                player1 = Player("X", "Player", human=True)
            if not player2:
                player2 = Player("O", "Computer", human=False)

        board = Board(int(board_width), int(board_height))
        game = TicTacToe(board, player1, player2, io)

        io.output("\nTo make a move, type the number of the cell you want to place your token in.\n")
        game.play()
        break

startup()

# TODO:

# 2. Refactor:
#   - Make computer an instance of the player class,take the logic out of the main game
#   - Take printing out of the game class
# 3. Check winner bugs:
#   - With uneven boards, diagonal check is weird: example 2x8, win is 2,10
#       > Different rules for non-square boards?
#   - If h > w, errors out: IndexError: index 3 is out of bounds for axis 1 with size 3
# 4. Error handling on input
# 5. Custom token support:
#   - Take printing X wins / 0 wins out of the winner check
#   - Amend winner check to detect win with any token
# 6. Add tests

