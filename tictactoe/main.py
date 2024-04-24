from tictactoe import TicTacToe
from board import Board
from player import Player
from iohandler import IOHandler
from constants import *
import os

def startup(io=IOHandler()):
    io.clear_screen()
    io.output_from_file("tictactoe/assets/hero_text.txt")

    player_choice = io.input_options("Press space > ", STARTUP_OPTS).strip()
    # EXIT
    if player_choice == STARTUP_OPTS[3]:
        io.output("\nThanks for playing <3")
        sys.exit(0)
    # SELECT BOARD SIZE
    elif player_choice == STARTUP_OPTS[1]:
        board_size = io.input_options("Select board size (press space): ", BOARD_SIZE_OPTS).strip()
        # Custom board size
        if board_size == BOARD_SIZE_OPTS[4]:
            board_width = io.input("Enter board width")
            board_height = io.input("Enter board height")
        else:
            board_width, board_height = board_size.split("x")
        board = Board(int(board_width), int(board_height))
        io.output("\nBoard size set to {}x{}\n".format(board_width, board_height))
        player1 = Player("X", "Player", human=True)
        player2 = Player("O", "Computer", human=False)

# SELECT GAME MODE
    elif player_choice == STARTUP_OPTS[2]:
        game_mode = io.input_options("Select game mode: ", GAME_MODE_OPTS).strip()
        # Computer VS Computer
        if game_mode == GAME_MODE_OPTS[2]:
            player1 = Player("X", "Computer1", human=False)
            player2 = Player("O", "Computer2", human=False)
        # Player VS Computer
        elif game_mode == GAME_MODE_OPTS[1]:
            name = io.input("Enter your name")
            token = io.input("Select your token").strip().upper()

            if not token: token = "X"
            if not name: name = "Player"

            if token == "X":
                player1 = Player(token, name, human=True)
                player2 = Player("O", "Computer", human=False)
            elif token == "O":
                player1 = Player("X", "Computer", human=False)
                player2 = Player(token, name, human=True)
        # Player VS Player
        elif game_mode == GAME_MODE_OPTS[0]:
            name1 = io.input("Enter Player1 name")
            name2 = io.input("Enter Player2 name")
            token1 = io.input("Select Player1 token").strip().upper()
            token2 = io.input("Select Player2 token").strip().upper()

            if not name1: name1 = "Player1"
            if not name2: name2 = "Player2"
            if not token1: token1 = "X"
            if not token2: token2 = "O"

            player1 = Player(token1, name1, human=True)
            player2 = Player(token2, name2, human=True)






        player1 = Player(tok, "Player1", human=True)
        player2 = Player("O", "Computer", human=False)
    # START GAME IN DEFAULT MODE
    elif player_choice == STARTUP_OPTS[0]:
        board_width, board_height = 3, 3
        player1 = Player("X", "Player", human=True)
        player2 = Player("O", "Computer", human=False)

    board = Board(int(board_width), int(board_height))
    game = TicTacToe(board, player1, player2, io)

    io.output("\nTo make a move, type the number of the cell you want to place your token in.\n")
    game.play()

startup()

# TODO:
# 1. Make startup options a loop so that one can go back once the board and game mode are customized
# 1. Make computer an instance of the player class,take the logic out of the main game
# 2. Before declaring a win it doesn't print the final board
# 3. With uneven boards, diagonal check is weird: example 2x8, win is 2,10
#   - Different rules for non-square boards?

