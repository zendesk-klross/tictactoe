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
        io.output("Player1 is {}".format(player1.name if player1 else "👤Player"))
        io.output("Player2 is {}".format(player2.name if player2 else "🤖Computer"))
        player_choice = io.input_options("Press space for options > ", STARTUP_OPTS).strip()

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
            io.output("\nBoard size set to {}x{}\n".format(board_width, board_height))
            continue

        # SELECT GAME MODE
        elif player_choice == STARTUP_OPTS[2]:
            game_mode = io.input_options("Select game mode: ", GAME_MODE_OPTS).strip()
            # Computer VS Computer
            if game_mode == GAME_MODE_OPTS[2]:
                player1 = Player("X", "🤖Computer1", human=False)
                player2 = Player("O", "🤖Computer2", human=False)
                continue
            # Player VS Computer
            elif game_mode == GAME_MODE_OPTS[1]:
                name = io.input("Enter your name")
                token = io.input("Select your token").strip().upper()

                if not token: token = "X"
                if not name: name = "👤Player"

                if token == "O":
                    player1 = Player("X", "🤖Computer", human=False)
                    player2 = Player(token, name, human=True)
                else:
                    player1 = Player(token, name, human=True)
                    player2 = Player("O", "🤖Computer", human=False)
            # Player VS Player
            elif game_mode == GAME_MODE_OPTS[0]:
                name1 = io.input("Enter Player1 name")
                token1 = io.input("Select Player1 token").strip().upper()
                name2 = io.input("Enter Player2 name")
                token2 = io.input("Select Player2 token").strip().upper()

                if not name1: name1 = "👤Player1"
                if not name2: name2 = "👤Player2"
                if not token1: token1 = "X"
                if not token2: token2 = "O"

                if token1 == "O":
                    player1 = Player(token2, name2, human=True)
                    player2 = Player(token1, name1, human=True)
                else:
                    player1 = Player(token1, name1, human=True)
                    player2 = Player(token2, name2, human=True)
            continue

        # START GAME
        elif player_choice == STARTUP_OPTS[0]:
            if not board_width or not board_height:
                board_width, board_height = 3, 3
            if not player1:
                player1 = Player("X", "👤Player", human=True)
            if not player2:
                player2 = Player("O", "🤖Computer", human=False)

        board = Board(int(board_height), int(board_width))
        game = TicTacToe(board, player1, player2, io)

        game.play()
        replay = io.input_options("Play again? ", ["Yes", "No"]).strip()
        if replay == "No":
            io.output("\nThanks for playing <3")
            break

startup()

# TODO:

# 3. Check winner weirdness?
#   - With uneven boards, diagonal check is weird: example 2x8, win is 2,10
#       > Different rules for non-square boards?
# 4. Error handling on input
#   - When press Enter, exits the programme
# 6. Add tests

