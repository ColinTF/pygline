#The imports we need
from turtle import pos
from pygame import time
import numpy as np


# test

# This class will be the parent object to everything that can be seen or does something in the game
# You can attach functionality to the object to make it do intresting stuff like a renderer
class GameObject:


    # Init the object with the time it was made and its name
    # Names should be unique
    def __init__(self, name, pos=None, tags=None):
        self._name = name
        self._creation_time = time.get_ticks()
        if tags is None:
            self.tags = []
        else:
            self.tags = tags

        if pos is None:
            self.position = np.zeros(2)
        else:
            self.position = pos
        self.velocity = np.zeros(2)
        self.acceleration = np.zeros(2)  

    def update():
        pass

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