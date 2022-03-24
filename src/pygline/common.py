"""
Common small classes and stuctures used throug out the whol package
"""

from dataclasses import dataclass, field
from collections.abc import Sequence
import numpy as np


@dataclass(order=True)
class Vertex:

    one = np.float32(1.0)
    """1.0 as a numpy float32"""

    x : float
    """X postion as a float"""
    y : float
    """Y postion as a float"""
    z : float = field(default=0.0)
    """Z postion as a flo  at"""

    r : float = field(default=0.0, compare=False)
    """Red color as a float"""
    g : float = field(default=0.0, compare=False)
    """Green color as a float"""
    b : float = field(default=0.0, compare=False)
    """Blue color as a float"""

    @property
    def coords(self):
        """The postions as a numpy array"""
        return np.array([self.x, self.y, self.z], dtype=np.float32)

    def set_coords(self, inp):
        """Use a tuple or list to set the coords"""
        # Make sure the values dont exceed 1.0
        # If its a single value set it to all
        if isinstance(inp, Sequence) and not isinstance(inp, str):
            self.x = min(np.float32(inp[0]), self.one)
            self.y = min(np.float32(inp[1]), self.one)
            if len(inp) >= 3:
                self.z = min(np.float32(inp[2]), self.one)
        else:
            value = min(np.float32(inp), self.one)
            self.x = value
            self.y = value
            self.z = value


    @property
    def color(self):
        """The colors as a numpy array"""
        return np.array([self.r, self.g, self.b], dtype=np.float32)

    def set_color(self, inp):
        """Use a tuple or list to set the color"""
        # Make sure the values dont exceed 1.0
        # If its a single value set it to all
        if isinstance(inp, Sequence) and not isinstance(inp, str):
            self.r = min(np.float32(inp[0]), self.one)
            self.g = min(np.float32(inp[1]), self.one)
            self.b = min(np.float32(inp[2]), self.one)
        else:
            value = min(np.float32(inp), self.one)
            self.r = value
            self.g = value
            self.b = value


    def copy(self):
        """Retuns a copy of the vertex"""
        return Vertex(self.x, self.y, self.z, self.r, self.g, self.b)

    def __getattr__(self, items):
        """Lets us retrive any values in any order as a numpy array"""
        attributes = np.zeros(len(items), dtype=np.float32)
        for i, val in enumerate(items):
            if val in 'xyzrgb':
                attributes[i] = self.__getattribute__(val)
            else:
                raise AttributeError
        return attributes

    def __setattr__(self, items, inp):
        """Lets us set any values in any order as a numpy array"""
        if items == 'coords':
            self.set_coords(inp)
        elif items == 'color':
            self.set_color(inp)
        elif len(items) <= 1:
            self.__dict__[items] = min(np.float32(inp), self.one)
        else:
            for i, val in enumerate(items):
                if val in 'xyzrgb':
                    self.__dict__[val] = min(np.float32(inp[i]), self.one)
                else:
                    raise AttributeError
