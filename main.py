"""
graphics engine for 2D games
"""
import os
import numpy as np
import cv2
from game import start_game, move_player


# title of the game window
GAME_TITLE = "Dungeon Explorer"

# map keyboard keys to move commands
MOVES = {
    "a": "left",
    "d": "right",
    "w": "up",
    "s": "down",

    "x": "cheat",
}

#
# constants measured in pixels
#
SCREEN_SIZE_X, SCREEN_SIZE_Y = 840, 640
TILE_SIZE = 64  # was: 64


def mouse_clicked(event,x,y,flags,param):
    """
    callback function: gets called automatically
    when something happens"""
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, y)
        # can use the game variable
        # attack(game, x, y)

def read_image(filename: str) -> np.ndarray:
    """
    Reads an image from the given filename and doubles its size.
    If the image file does not exist, an error is created.
    """
    img = cv2.imread(filename)  # sometimes returns None
    if img is None:
        raise IOError(f"Image not found: '{filename}'")
    img = np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))  # double image size
    return img


def read_images():
    return {
        filename[:-4]: read_image(os.path.join("tiles", filename))
        for filename in os.listdir("tiles")
        if filename.endswith(".png")
    }


def draw_tile(frame, x, y, image, xbase=0, ybase=0):
    # calculate screen position in pixels
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    # copy the image to the screen
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = image


def draw(game, images):
    # initialize screen
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    # draw dungeon tiles
    for y, row in enumerate(game.level):
        for x, tile in enumerate(row):
            if tile == ".":
                draw_tile(frame, x=x, y=y, image=images["floor"])
            if tile == "s":
                draw_tile(frame, x=x, y=y, image=images["statue"])
            if tile == "t":
                draw_tile(frame, x=x, y=y, image=images["trap"])

    # draw player
    draw_tile(frame, x=game.x, y=game.y, image=images["player"])

    for dmg in game.damages:
        if dmg.counter > 0:
            #draw_tile(frame, x=dmg.x, y=dmg.y, image=images[dmg.image_name])
            cv2.putText(frame,
                dmg.text,
                org=(TILE_SIZE*dmg.x, TILE_SIZE*dmg.y),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5,
                color=(128, 128, 255),
                thickness=4,
                )
            dmg.counter -= 1

    # draw a heart at a pixel position
    draw_tile(frame, x=0, y=0, image=images["heart"], xbase=601, ybase=0)
    # display complete image
    cv2.imshow(GAME_TITLE, frame)


def handle_keyboard(game):
    """keys are mapped to move commands"""
    code = cv2.waitKey(1) & 0xFF
    #if code != 255:  # 255 means "no key pressed"
    #    print(code)
    if code == 81:  # left arrow key on my machine, yours might be different
        key = "a"
    else:
        key = chr(code)
    if key == "q":
        game.status = "exited"
    if key in MOVES:
        move_player(game, MOVES[key])  # sends a DungeonGame to move_player function


# game starts
images = read_images()
game = start_game()  # game is a DungeonGame

cv2.namedWindow(GAME_TITLE)
cv2.setMouseCallback(GAME_TITLE, mouse_clicked)

while game.status == "running":

    draw(game, images)
    handle_keyboard(game)

cv2.destroyAllWindows()
