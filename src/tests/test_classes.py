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


class Test_Vertex:

    def test_one(self):

        print("\n\n")

        vert1 = Vertex(1, 2, 3)

        vert1.color = 1, 0.5, 3
        vert1.z = 0.01
        vert1.coords = -.5, 0.5

        vert2 = vert1.copy()
        vert1.z = 0.07
        vert2.x = 0.35

        vert3 = Vertex([0.2, 0.2, 0.2])

        vert4 = Vertex(1)
        print(vert4)

        print(vert1)
        print(vert2)
        print(vert3)
        print(vert3.bxy)
        vert4 = Vertex(1, 2, 3)
        print(vert4)
        print(vert4.xyz)
        vert4.xyz *= 1.2
        print(vert4.__dict__)
        # assert Vertex(0.2, 0.2) > Vertex(0, 0.5) == False

    def test_two(self):

        assert Vertex(1) > 0.5
        assert Vertex(1) > Vertex(0.5)
        assert Vertex(1, 5, 3) > Vertex(3, 2, 1, b=2.0)
        assert Vertex(2, 4, 5) - Vertex(1, 3, 5) == Vertex(1, 1, 0)
        assert Vertex(1, 2, 3) + Vertex(1, 2, 3) == Vertex(2, 4, 6)
        assert Vertex(5, 2, 8) * Vertex(1, 2, 3) == Vertex(5, 4, 24)
        assert Vertex(12, 16, 24) * 0.5 == Vertex(6, 8, 12)
        assert Vertex(12, 16, 24) / 2 == Vertex(6, 8, 12)
        assert Vertex(2, 4, 6) + [1, 2] == Vertex(3, 6, 6)
        assert Vertex(2, 4, 6) * [1, 2] == Vertex(2, 8, 6)
        assert Vertex(5, 2, 8) / Vertex(1, 2, 3) == Vertex(5, 1, 8/3)