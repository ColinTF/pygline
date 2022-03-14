# Make our imports we need
import numpy as np
import pygame as pg
import os

import random

#import our own custom classes
import gamegine as gg


# Define some paramters for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# This will be where our game takes place
def game(screen):

    # Create the main scene game
    scene1 = gg.Scene()

    print(f"\nStarting Game at Time: {scene1.last_time / 1000}s \n\n")

    mover = scene1.add_object(gg.GameObject('mover', pos=[0, SCREEN_HEIGHT/2-50], tags=['fast']), 'objects')
    mover.add_component('renderer', gg.renderer(mover, screen, size=[100, 100]))
    mover.add_component('physics', gg.physics(mover, mass=5))

    # When the scene return false end the main game loop
    running = True
    spawn_time = 250
    spawn_timer = 0
    i = 0
    while running:

        # Make the changes we want to make

        if mover.position[0] < SCREEN_WIDTH/2-50:
            mover.physics.force([20, 0], 100)
        else:
            mover.physics.force([-20, 0], 100)
            

        if scene1.time > spawn_timer:
            print(mover.physics.velocity)
            spawn_timer = scene1.time + spawn_time
            i += 1

            bullet = scene1.add_object(gg.GameObject('bullet'+str(i), pos=[mover.position[0]+50, SCREEN_HEIGHT/2-50]), 'bullets')
            bullet.add_component('renderer', gg.renderer(bullet, screen, size=[10, 10]))
            bullet.add_component('physics', gg.physics(bullet, mass=1))
            bullet.physics.force([0, -25], 100)
            bullet.renderer.surf.fill((255, 0, 0))

        # Update the scene by passing events to it
        running = scene1.update(pg.event.get(), screen)

        
        # Push updates to display
        pg.display.flip()

    print(scene1)

    # after our game loop ends we must quit pygame
    print(f"\n\nEnding Game at Time: {scene1.last_time / 1000}s \n")

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