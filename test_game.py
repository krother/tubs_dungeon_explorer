"""
install pytest with

    python -m pip install pytest

run the test with:

    python -m pytest -s test_game.py 

"""
from game import move_player, DungeonGame, parse_level


def test_move():
    """the player can move right"""
    game = DungeonGame(
        x=1,
        y=1,
        level=parse_level(
            [
                "....",
                ".s..",
                "....",
                "....",
            ]),
            teleporters=[]
    )
    move_player(game, "right")
    assert game.x == 2  # has to be two, otherwise the test fails
    assert game.y == 1


def test_collect_coin():
    """the player can move right"""
    game = DungeonGame(
        x=1,
        y=1,
        level=parse_level(
            [
                "....",
                ".s..",
                ".€..",
                "....",
            ]),
            teleporters=[]
    )
    move_player(game, "down")
    assert game.coins == 1
