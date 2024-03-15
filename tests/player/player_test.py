import tictactoe.player


def test_initialization_with_token_and_no_name():
    token = 'X'
    player = tictactoe.player.Player(token)
    assert player.token == token
    assert player.name == "Player"


def test_initialization_with_token_and_name():
    token = 'X'
    name = "ana"
    player = tictactoe.player.Player(token, name)
    assert player.token == token
    assert player.name == name
