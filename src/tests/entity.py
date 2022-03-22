"""This file will manage all the "user" built classes outside of the core game engine for testing"""

import numpy as np
import pygline as pg

from pygline import locals as ggls

class Player(pg.GameObject):
    
    def __init__(self, name, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.mesh =  pg.components.Mesh(self, scale=[0.01, 0.01], primitive_shape=ggls.PRIMITE_SQUARE)
        self.rigidbody = pg.components.rigidbody(self, mass=5)

        self.speed = 200

    def input(self, event):
        pass