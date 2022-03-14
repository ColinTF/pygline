# Make our imports we need
import numpy as np
import pygame as pg
import os

import random

#import our own custom classes
import scene
import gameObjects as obj


# Define some paramters for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# This will be where our game takes place
def game(screen):

    # Create the main scene game
    scene1 = scene.Scene()

    print(f"\nStarting Game at Time: {scene1.last_time / 1000}s \n\n")

    c = scene1.add_object(obj.GameObject('mover', pos=[0, SCREEN_HEIGHT/2-50], tags=['fast']), 'objects')
    c.add_components(obj.renderer(c, size=[100, 100]))
    c.add_components

    # When the scene return false end the main game loop
    running = True
    spawn_time = 250
    spawn_timer = 0
    while running:
        # Update the scene by passing events to it
        running = scene1.update(pg.event.get(), screen)
        if c.position[0] < SCREEN_WIDTH/2-50:
            c.physics.accelerate([20, 0], 100)
        else:
            c.physics.accelerate([-20, 0], 100)
        if scene1.time > spawn_timer:
            spawn_timer = scene1.time + spawn_time
            d = scene1.add_object(obj.GameObject(str(scene1.time+random.randint(0, 1000)), pos=[c.position[0]+50, SCREEN_HEIGHT/2-50], tags=['cool', 'fast']), 'dots')
            d.render = obj.renderer(d, size=[5, 5])
            d.add_components(d.render)
            d.physics = obj.physics(d, mass=10)
            d.add_components(d.physics)
            d.physics.accelerate([0, -25], 200)
        
        # Push updates to display
        print(c.physics.velocity)
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