### This file will manage all the user built classes outside of the core game engine
### Do not add game engine features here

import numpy as np
from gamegine import gameobject as go

class Player(go.GameObject):
    
    def __init__(self, name, screen, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.add_component('renderer', gg.mesh(self, screen, size=[100, 100]))
        self.add_component('physics', gg.physics(self, mass=5))

        self.speed = 200

    def input(self, event):
        if event.keys[K_w]:
            self.physics.add_force([0, -self.speed])
        if event.keys[K_d]:
            self.physics.add_force([self.speed, 0])
        if event.keys[K_a]:
            self.physics.add_force([-self.speed, 0])
        if event.keys[K_s]:
            self.physics.add_force([0, self.speed])

class Player2(go.GameObject):
    
    def __init__(self, name, screen, pos=np.zeros(2), tags=[]):
        super().__init__(name, pos=pos, tags=tags)
        self.add_component('renderer', gg.mesh(self, screen, size=[100, 100]))
        self.add_component('physics', gg.physics(self, mass=5))

        self.speed = 200

    def input(self, event):
        if event.keys[K_UP]:
            self.physics.add_force([0, -self.speed])
        if event.keys[K_RIGHT]:
            self.physics.add_force([self.speed, 0])
        if event.keys[K_LEFT]:
            self.physics.add_force([-self.speed, 0])
        if event.keys[K_DOWN]:
            self.physics.add_force([0, self.speed])