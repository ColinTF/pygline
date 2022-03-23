"""
Our main test which we will build a test game in as well as other tests
"""

# Make our imports we need
import numpy as np

import random
import os

# import our own game engine
# from src.gamegine import engine

import pygline as pg


#import our own custom classes
# import entity as ent
from tests import entity as ent


# Define some fixed paramters for the game
WIDTH = 800
HEIGHT = 800

# This will be where our game takes place
class Test_Main:


    def test_start_game(self):

        print("\n\n")
        
        # Create the path to the resources folder
        path = os.getcwd()
        resource_path = "src\\tests\\resources"
        resource_path_abs = os.path.join(path, resource_path)

        scene1 = pg.Scene()

        player1 = ent.Player('Player', [0, 0])

        scene1.add_object(player1, 'Players')

        game = pg.Game("Test Game With pygline", (WIDTH, HEIGHT), resource_path_abs)

        game.set_scene(scene1)

        game.start_game_loop()

        game.end()

    def test_multiple_characters(self):

        print("\n\n")
        
        # Create the path to the resources folder
        path = os.getcwd()
        resource_path = "src\\tests\\resources"
        resource_path_abs = os.path.join(path, resource_path)

        scene1 = pg.Scene()

        for i in range(0, 5000):
            player = ent.Player('Player' + str(i), 2*np.array([random.random()-0.5, random.random()-0.5]))
            scene1.add_object(player, 'Players')

        game = pg.Game("Test Game With pygline", (WIDTH, HEIGHT), resource_path_abs)

        game.set_scene(scene1)

        game.start_game_loop()

        game.end()

    def test_scene_swap(self):

        print("\n\n")
        
        # Create the path to the resources folder
        path = os.getcwd()
        resource_path = "src\\tests\\resources"
        resource_path_abs = os.path.join(path, resource_path)

        scene1 = pg.Scene()
        scene2 = pg.Scene()

        player1 = ent.Player('Player', [0, 0])
        scene1.add_object(player1, 'Players')

        player2 = ent.Player('Player2', [0.5, 0.5])
        scene2.add_object(player2, 'Players')

        game = pg.Game("Test Game With pygline", (WIDTH, HEIGHT), resource_path_abs)

        game.set_scene(scene1)
        game.set_scene(scene2)

        game.start_game_loop()

        game.end()