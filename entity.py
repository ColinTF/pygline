### This file will manage all the user built classes outside of the core game engine
### Do not add game engine features here

import pygame as pg
import numpy as np
import gamegine as gg

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(gg.GameObject):
    
    def __init__(self, name, screen, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.add_component('renderer', gg.renderer(self, screen, size=[100, 100]))
        self.add_component('physics', gg.physics(self, mass=5))