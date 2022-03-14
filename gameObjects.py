#The imports we need
import pygame as pg
import numpy as np

# Components are attached to objects to make them unqiue and interact
class component:

    def __init__(self, owner):
        self.owner = owner

    def update(self, delta_time):
        pass

# Allow the object to be re
# ndered to the screen
class renderer(component):

    def __init__(self, owner, output, size=[50, 50], rel_location=np.zeros(2), color=(255,255,255)):
        super(renderer, self).__init__(owner)

        self.surf = pg.Surface(size)
        self.surf.fill(color)

        self.rel_location = rel_location

        self.rect = self.surf.get_rect()

        self.output = output

    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super(renderer, self).update(delta_time)

        self.rect.topleft = self.owner.position + self.rel_location
        self.output.blit(self.surf, self.rect)

# Allow the object to interact with the world
class physics(component):

    def __init__(self, owner, mass=1, collision=True, gravity=False, passive=False):
        super(physics, self).__init__(owner)

        self.mass = mass

        # Add appropriate tags to parent
        if collision:
            self.owner.add_tag('collision')
        if gravity:
            self.owner.add_tag('gravity')
        if passive:
            self.owner.add_tag('passive')

        self.acceleration = np.zeros(2)
        self.velocity = np.zeros(2)

    # Update the postion using math and delta time
    def update(self, delta_time):
        super(physics, self).update(delta_time)

        self.velocity += self.acceleration * delta_time
        self.owner.position += self.velocity * delta_time

    # Apply a force to an object at it CM and calculate the resulting acceleration based on mass
    def force(self, ammount, max_accel):

        # Take the max between the normlized expected change and max then multiply it by the direction vector
        change = self.acceleration + ammount
        norm = np.linalg.norm(change)
        force = np.amin([norm, np.abs(max_accel)])
        if norm >= 0.01:
            self.acceleration = (force*change/norm) / self.mass
        
        

# This class will be the parent object to everything that can be seen or does something in the game
# You can attach functionality to the object to make it do intresting stuff like a renderer
class GameObject:

    # The default tags to use
    default_tags = ['updates']

    # Init the object with the time it was made and its name
    # Names should be unique
    def __init__(self, name, pos=np.zeros(2), tags=[]):
        self._name = name
        self._creation_time = pg.time.get_ticks()
        self.tags = []
        self.tags.extend(self.default_tags)

        self.update_responsibilities = []

        self.position = pos

    # Update all components
    def update(self, delta_time):
        for resposibilty in self.update_responsibilities:
            resposibilty(delta_time)

    # Add components as atrributes and add their update functions to the responsibilties list
    def add_component(self, name, component):
        setattr(self, name, component)
        self.update_responsibilities.append(component.update)


    # These next function allow for tag managment
    # say we want to loop through all our objects and
    # only do something to certain ones
    # might be a good idead to store lists of all objects with a certain tag
    def add_tag(self, tag):
        self.tags.append(tag)

    # Check if a set of tags or tag is assigned
    def has_tags(self, tags):
        if isinstance(tags, list):
            return all(x in self.tags for x in tags)
        else: 
            return tags in self.tags

    def rm_tag(self, tag):
        self.tags.remove(tag)

    def get_tags(self):
        return self.tags

    def kill(self, announce=False):
        if announce:
            print(f"'{self._name}' has been killed and removed")

    # Functions that add functionalty to print the class
    def __repr__(self):
        return f"{self._name}, {self._creation_time / 1000.0} s"
    def __str__(self):
        return f"{self._name}"

    # Use these for comparing objects and hasing

    def __key(self):
        return (self._name, self._creation_time)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, GameObject):
            return self.__key() == other.__key()
        return NotImplemented