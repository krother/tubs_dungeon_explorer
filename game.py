"""
the Dungeon Explorer game logic
"""
import random
from levels import LEVEL_ONE
from model import DungeonGame, Teleporter, DamageIcon

XLIMIT = 9
YLIMIT = 9


def move_player(game: DungeonGame, direction: str):
    """Things that happen when the player walks on stuff"""
    # cheat mode
    if direction == "cheat":
        game.health = 1_000_000
        game.cheat_mode = True
        return
    
    x = game.x  # temporary variable or helper variable
    y = game.y

    if direction == "right" and (x < XLIMIT):
        x = x + 1
    elif direction == "left" and (x > 0):
        x = x - 1
    elif direction == "up" and (y > 0):
        y = y - 1
    elif (direction == "down") and (y < YLIMIT):
        y = y + 1

    for t in game.teleporters:
        if x == t.x1 and y == t.y1:  # teleports in one direction
            game.x = t.x2
            game.y = t.y2
        elif x == t.x2 and y == t.y2:  # teleports in the other direction
            game.x = t.x1
            game.y = t.y1

    if game.level[y][x] == "€":
        game.coins += 1

    if game.level[y][x] == "t":
        game.health -= 1
        damage = DamageIcon(
            x=x,
            y=y,
            image_name=random.choice(["prompt_no", "prompt_yes"]),
            counter=100,
            text=random.choice(["Ouch", "aah", "ZAP", "BOOM"]),
        )
        game.damages.append(damage)


    can_be_walked_on = ".sk^vt"  # floor, statue, key, stairs up and down
    if game.level[y][x] in can_be_walked_on or game.cheat_mode:
        game.x = x
        game.y = y


def start_game():
    return DungeonGame(
        x=8,
        y=1,
        level=LEVEL_ONE,
            teleporters=[
                Teleporter(x1=1, y1=1, x2=8, y2=8),
            ],
    )
