### This file will manage all the user built classes outside of the core game engine
### Do not add game engine features here

import numpy as np
import pygline as pg

from pygline import locals as ggls

class Player(pg.GameObject):
    
    def __init__(self, name, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.mesh =  pg.components.mesh(self, scale=[0.5, 0.5], primitive_shape=ggls.PRIMITE_SQUARE)
        self.rigidbody = pg.components.rigidbody(self, mass=5)

        self.speed = 200

    def input(self, event):
        pass