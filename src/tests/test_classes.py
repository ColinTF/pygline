# Make our imports we need
import numpy as np

import random
import os

# import our own game engine
# from src.gamegine import engine

import pygline as pg
from pygline.common import Vertex


#import our own custom classes
# import entity as ent
from tests import entity as ent


class Test_Classes:

    def test_vertex_one(self):

        print("\n\n")

        vert1 = Vertex(1, 2, 3)

        vert1.color = 1, 0.5, 3
        vert1.z = 0.01
        vert1.coords = -.5, 0.5

        vert2 = vert1.copy()
        vert1.z = 0.07
        vert2.x = 0.35

        vert3 = Vertex(0.2, 0.2, 0.2, b=0)

        print(vert1)
        print(vert2)
        print(vert3)
        print(vert3.bxy)
        # assert Vertex(0.2, 0.2) > Vertex(0, 0.5) == False

    def test_vertex_two(self):

        print("\n\n")

        vert1 = Vertex(7, 12, 3)
        vert1.xr = 0.5, 0.02

        print(vert1)
        print(vert1.xyr)
        print(vert1.coords)
        vert1.coords = 0.03, 0.97
        print(vert1.coords)
        vert1.coords = 0.5
        print(vert1.coords)
        vert1.rg = 0.1 , 0.3
        print(vert1.color)