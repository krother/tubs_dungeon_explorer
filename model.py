"""
Data model for the dungeon game
"""
from pydantic import BaseModel


class DamageIcon(BaseModel):
    x: int
    y: int
    image_name: str
    counter: int
    text: str

class Teleporter(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    level: list[list[str]]
    teleporters: list[Teleporter]
    coins: int = 0
    health: int = 10
    damages: list[DamageIcon] = []
    cheat_mode: bool = False
