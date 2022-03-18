# Make our imports we need
import numpy as np
import pygame as pg
import os

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


import random

#import our own game engine
import gamegine as gg

#import our own custom classes
import entity as ent


# Define some paramters for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Shows the screen
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

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
        pass

    # after our game loop ends we must quit pygame
    print(f"\n\nEnding Game at Time: {scene1.time}s \n")

# Our main function
def main():

    # Clear terminal
    # os.system('cls' if os.name == 'nt' else 'clear')

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutInitWindowPosition(0,0)

    window = glutCreateWindow("Game")
    glutDisplayFunc(showScreen)
    #glutIdleFunc(showScreen)
    glutMainLoop()
    


if __name__ == "__main__":
    main()