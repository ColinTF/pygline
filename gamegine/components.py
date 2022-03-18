import numpy as np
from gamegine.locals import *

class component:
    """
    Components are attached to objects to make them unqiue and interact

    Components can be defined by the user but built-ins include:
        - Physics
        - Renderer
        - #TODO add more components
    """

    def __init__(self, owner):
        self.owner = owner

    def update(self, delta_time):
        pass

    def kill(self):
        pass

# Allow the object to be re
# rendered to the screen
class mesh(component):

    def __init__(self, owner, rel_location : np.ndarray = np.zeros(2), color : tuple[float] = (1.0, 1.0, 1.0)):
        super().__init__(owner)

        self.rel_location = rel_location

        self.rotation = 0

    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super().update(delta_time)

        if self.rotation != self.owner.rotation:
            self.rotation = self.owner.rotation


# Allow the object to interact with the world
class physics(component):

    def __init__(self, owner, mass=1, friction=0.1, collision=True, gravity=False, passive=False):
        super(physics, self).__init__(owner)

        self.mass = mass

        # Add appropriate tags to parent
        if collision:
            self.owner.add_tag('collision')
        if gravity:
            self.owner.add_tag('gravity')
        if passive:
            self.owner.add_tag('passive')

        self.friction = friction

        self.forces = np.array([0, self.mass * GRAVITY]) if self.owner.has_tags(['gravity']) else np.zeros(2)
        self.acceleration = np.zeros(2)
        self.velocity = np.zeros(2)

    # Update the postion using math and delta time
    def update(self, delta_time):
        super(physics, self).update(delta_time)

        self.forces *= (1 - self.friction)

        self.acceleration = self.forces / self.mass
        self.velocity += self.acceleration * delta_time
        self.owner.position += self.velocity * delta_time

    # Set the force at CM
    def set_force(self, force):

        # Make sure the force has a gravity applied if applicable
        self.forces = np.add(force, [0, (self.mass * GRAVITY) if self.owner.has_tags(['gravity']) else 0])

    # Add Force at CM
    def add_force(self, force):

        if isinstance(force, np.ndarray):
            self.forces += force
        else:
            self.forces += np.array(force)

    # Rotate the object
    def rotate(self, degrees):

        self.owner.rotation += degrees