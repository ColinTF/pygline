# Make our imports we need
import numpy as np
import pygame as pg
import os

import random

#import our own game engine
import gamegine as gg

#import our own custom classes
import entity as ent


# Define some paramters for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# This will be where our game takes place
def game(screen):

    # Create the main scene game
    scene1 = gg.Scene()

    print(f"\nStarting Game at Time: {scene1.time}s \n\n")

    player1 = ent.Player('Player1', screen, pos=[0, SCREEN_HEIGHT])
    scene1.add_object(player1, 'players')
    scene1.add_event_handler(gg.KEYHELD, player1.input)
    player1.renderer.surf.fill((0,0,255))

    player2 = ent.Player2('Player2', screen, pos=[0, 0])
    scene1.add_object(player2, 'players')
    scene1.add_event_handler(gg.KEYHELD, player2.input)

    player1.physics.rotate(12)

    player1.physics.rotate(12)

    player1.physics.rotate(-12)

    # When the scene return false end the main game loop
    running = True
    spawn_time = 1
    spawn_timer = 0
    i = 0
    while running:

        # Make the changes we want to make

        # if player1.position[0] < SCREEN_WIDTH/2-50:
        #     player1.physics.set_force([5000, 0])
        # else:
        #     player1.physics.set_force([-5000, 0])
            

        # if scene1.time > spawn_timer:
        #     # print(player1.physics.velocity)
        #     spawn_timer = scene1.time + spawn_time
        #     i += 1

        #     # print(player1.physics.acceleration)

        #     bullet = scene1.add_object(gg.GameObject('bullet'+str(i), pos=[player1.position[0]+50, player1.position[1]+50]), 'bullets')
        #     bullet.add_component('renderer', gg.renderer(bullet, screen, size=[10, 10]))
        #     bullet.add_component('physics', gg.physics(bullet, mass=1, friction=0.05, gravity=True))
        #     bullet.physics.add_force([0, -5000])
        #     bullet.renderer.surf.fill((255, 0, 0))

        # # Update the scene by passing events to it
        running = scene1.update(pg.event.get(), screen)

        # for bullet in scene1.get_objects(groups=['bullets']):
        #     if (scene1.time - bullet._creation_time) > 12:
        #         scene1.rm_objects([bullet])

        
        # Push updates to display
        pg.display.flip()

    print(scene1)

    # after our game loop ends we must quit pygame
    print(f"\n\nEnding Game at Time: {scene1.time}s \n")

# Our main function
def main():

    # Clear terminal
    # os.system('cls' if os.name == 'nt' else 'clear')

    # Initilize the game and create the window we will display to
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Start the game and tell it attach it to the screen we just made
    game(screen)

    # End pygame
    pg.quit()


if __name__ == "__main__":
    main()