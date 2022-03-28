"""This file will manage all the "user" built classes outside of the core game engine for testing"""

import numpy as np
import pygline as pg

from pygline import locals as pgl
from pygline.logic.event import *

class Player(pg.GameObject):
    
    def __init__(self, name, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.mesh =  pg.components.Mesh(scale=[0.01, 0.01], primitive_shape=pg.components.Mesh.PRIMITIVE_SQUARE)
        self.rigidbody = pg.components.RigidBody(mass=5)

        self.speed = 200

    # This function is special its named tells the engine that it is an event listener
    def on_key_event(self, event : KeyEvent):
        if event.key == glfw.KEY_W and event.action == glfw.PRESS:
            self.position[0] += 100