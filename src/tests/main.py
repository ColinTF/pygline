# Make our imports we need
import numpy as np

import random
import os

# import our own game engine
# from src.gamegine import engine
from gamegine import engine


#import our own custom classes
# import entity as ent
from tests import entity as ent


# Define some fixed paramters for the game
WIDTH = 800
HEIGHT = 800

# This will be where our game takes place
def main():

    path = os.getcwd()
    resource_path = "tests\\resources"
    resource_path_abs = os.path.join(path, resource_path)

    game = engine.Game("Gamegine", (WIDTH, HEIGHT))

    game.set_resource_dir(resource_path_abs)
    game.load()

    game.start_game_loop()

    game.end()


if __name__ == "__main__":
    main()