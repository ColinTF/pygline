# Make our imports we need
import numpy as np

import random

#import our own game engine
import gamegine as gg

#import our own custom classes
import entity as ent


# Define some fixed paramters for the game
WIDTH = 800
HEIGHT = 800

# This will be where our game takes place
def main():

    game = gg.Game("Gamegine", (WIDTH, HEIGHT))

    game.loop()

    game.end()

    # Create the main scene game
    # scene1 = gg.Scene()

    # print(f"\ntarting Game at Time: {scene1.time}s \n\n")

    # player1 = ent.Player('Player1', screen, pos=[0, SCREEN_HEIGHT])
    # scene1.add_object(player1, 'players')
    # scene1.add_event_handler(gg.KEYHELD, player1.input)
    # player1.renderer.surf.fill((0,0,255))

    # player2 = ent.Player2('Player2', screen, pos=[0, 0])
    # scene1.add_object(player2, 'players')
    # scene1.add_event_handler(gg.KEYHELD, player2.input)

    # player1.physics.rotate(12)

    # player1.physics.rotate(12)

    # player1.physics.rotate(-12)

    # # When the scene return false end the main game loop
    # running = True
    # while running:
    #     pass

    # # after our game loop ends we must quit pygame
    # print(f"\n\nEnding Game at Time: {scene1.time}s \n")


if __name__ == "__main__":
    main()