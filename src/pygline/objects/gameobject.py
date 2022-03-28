from pygline.objects import *
import numpy as np

from pygline.logic.event import *

from glfw import get_time

class GameObject:
    """
    Master class for all objects

    All things that move/interact/rendered should be a gameobject. For example, the player, a tree, or even a force field!

    Here is what GameObjects can do:
        - have one parent and may have multiple children
        - be organized with tags
        - own components like `Mesh`, `RigidBody`, etc.

    Warnings:
        - every name *MUST* be unique. There is built-in methods to do this
    """

    # The default tags to use
    default_tags = ['updates']

    # Init the object with the time it was made and its name
    # Names should be unique
    def __init__(self, name : str, pos : np.ndarray = np.zeros(2), tags : list[str] = []):
        """
        Create a blank game object

        Args:
            - name: unique string to identify the object
            - pos: starting position as a 2d numpy array
            - tags: list of strings to catagorize the object with
        """
        self._name = name
        self._creation_time = get_time()
        self.tags = []
        self.tags.extend(self.default_tags)

        self.components = []
        self.update_responsibilities = []

        self.position = pos
        self.rotation = 0

    # Update all components
    def update(self, delta_time):
        for resposibilty in self.update_responsibilities:
            resposibilty(delta_time)

    # Add components as atrributes and add their update functions to the responsibilties list
    def add_component(self, name : str, component: components.component):
        setattr(self, name, component)
        self.components.append(name)
        self.update_responsibilities.append(component.update)

    def rm_component(self, name : str, component: components.component):
        self.components.remove(name)
        self.component.kill()
        self.update_responsibilities.remove(component.update)
        delattr(self, name)
        


    # These next function allow for tag managment
    # say we want to loop through all our objects and
    # only do something to certain ones
    # might be a good idead to store lists of all objects with a certain tag
    def add_tag(self, tag: str):
        self.tags.append(tag)

    # Check if a set of tags or tag is assigned
    def has_tags(self, tags: list[str]) -> bool:
        if isinstance(tags, list):
            return all(x in self.tags for x in tags)
        else: 
            return tags in self.tags

    def rm_tag(self, tag: str):
        self.tags.remove(tag)

    def get_tags(self) -> list[str]:
        return self.tags

    def kill(self, announce : bool = False):
        if announce:
            print(f"'{self._name}' has been killed and removed")
        for comp in self.components:
            self.components.remove(comp)

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