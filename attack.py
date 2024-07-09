"""
Do a Spin Attack
================

0. player presses the "attack" key
1. go through all four directions
2. calculate the next position in that directions
3. check if there is a skeleton in the next position
   3a. no skeleton -> do nothing
   3b. skeleton -> hurt the skeleton by X damage
4. remove dead skeletons
"""
# step 1: go through all four directions
for direction in ["up", "down", "left", "right"]:
    # step 2: calculate the next position
    newx, newy = get_next_position(game.x, game.y, direction)
    # step 3: check if there is a skeleton
    for s in game.skeletons:
        if newx == s.x and newy == s.y:
            # found a skeleton
            s.health -= 34

# step 4: remove dead skeletons
new_skeletons = []
for s in game.skeletons:
    if s.health > 0:
        new_skeletons.append(s)
game.skeletons = new_skeletons
    