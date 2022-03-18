# Make our imports we need
import numpy as np

import random

#import our own game engine
from ..src.gamegine import Game

#import our own custom classes
import entity as ent


# Define some fixed paramters for the game
WIDTH = 800
HEIGHT = 800

# This will be where our game takes place
def main():

    game = Game("Gamegine", (WIDTH, HEIGHT))

    game.start_game_loop()

    game.end()


if __name__ == "__main__":
    main()