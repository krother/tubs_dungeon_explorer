
from model import DungeonGame, Teleporter, DamageIcon


def parse_level(level):
    return [list(row) for row in level]


LEVEL_ONE = parse_level(
    [
        "..........",
        "..........",
        "..........",
        "..........",
        "...s..s...",
        "..........",
        ".tttttttt.",
        ".tttttttt.",
        ".tttttttt.",
        "..........",
    ]
)

LEVEL_TWO = parse_level(
    [
        "##########",
        "..........",
        "..........",
        "..........",
        "...s..s...",
        "..........",
        ".tttttttt.",
        ".tttttttt.",
        ".tttttttt.",
        "##########",
    ]
)
