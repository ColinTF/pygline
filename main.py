# Make our imports we need
import numpy as np
import pygame as pg
import os

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

    c = obj.GameObject("Colin")
    b = obj.GameObject("Ben")

    orange = obj.GameObject("Fruit2")

    scene1.add_object(c, "People")
    c.add_tag('blue')
    scene1.add_object(b, "People")
    scene1.add_object(obj.GameObject("Fruit1"), "main")
    scene1.add_object(orange, "main")
    orange.add_tag('tasty')
    scene1.add_object(obj.GameObject("Number"), "ints")
    scene1.get_objects(groups=['main'])['Fruit1'].add_tag('blue')
    scene1.add_object(obj.GameObject("Float"), "floats")
    scene1.get_objects(groups=['floats'])['Float'].add_tag('blue')

    scene1.rm_objects([c, b], announce=True)
    scene1.rm_objects(["Number", b], announce=True)

    print(scene1.get_objects(names=['Fruit1', 'Fruit2']))
    print(scene1.get_objects(tags=['blue'], groups=['People', 'ints', 'main'], op='or'))
    print(scene1.get_objects(tags=['tasty']))

    scene1.move_object(orange, 'default')
    orange.add_tag('medium')

    scene1.merge_group('floats', 'main')
    scene1.merge_group('main')


    # print(scene1)

    # When the scene return false end the main game loop
    running = True
    while running:
        # Update the scene by passing events to it
        running = scene1.update(pg.event.get())
        # Push updates to display
        pg.display.flip()

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