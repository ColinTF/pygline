"""
Common small classes and stuctures used throug out the whol package
"""

from dataclasses import dataclass, field
import numpy as np
from sympy import GoldenRatio


@dataclass(order=True)
class Vertex:

    x : float
    """X postion as a float"""
    y : float
    """Y postion as a float"""

    r : float = field(compare=False)
    """Red color as a float"""
    g : float = field(compare=False)
    """Green color as a float"""
    b : float = field(compare=False)
    """Blue color as a float"""

    @property
    def coords(self):
        """The postions as a numpy array"""
        return np.array([self.x, self.y], dtype=np.float32)

    @coords.setter
    def coords(self, inp):
        """Use a tuple or list to set the coords"""
        # Make sure the values dont exceed 1.0
        self.coords =  np.array([max(inp[0], 1.0), max(inp[1], 1.0)], dtype=np.float32)


    @coords.deleter
    def coords(self):
        del self.x
        del self.y


    @property
    def color(self):
        """The colors as a numpy array"""
        return np.array([self.r, self.g, self.b], dtype=np.float32)

    @color.setter
    def color(self, inp):
        """Use a tuple or list to set the color"""
        # Make sure the values dont exceed 1.0
        self.color =  np.array([max(inp[0], 1.0), max(inp[1], 1.0), max(inp[2], 1.0)], dtype=np.float32)


    @color.deleter
    def color(self):
        del self.r
        del self.g
        del self.b
