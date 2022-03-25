"""
Common classes and stuctures used through out the whole package
"""

from collections.abc import Sequence
import numpy as np
    

class Vertex:
    """

    # VERTEX

    The vertex class is a fundemental, versatille and easy to use class containing positional and color data.
    The data is stored as x,y,z,r,g,b attributes. However the data can be accessed and modified in a variety of ways.

    Attributes:
        - x,y,z : np.float32 - 3d coordinates of vertex
        - r,g,b : np.float32 - color of vertex

    Methods:
        - copy() -> Vertex - returns a copy of the vertex
        - magnitude() -> np.float32 - returns the magnitude of the vertex
        - brightness() -> np.float32 - returns the brightness of the vertex
        - normalize() -> None - normalizes the vertex to a unit vector

    ---

    ### Usage

    Groups of vertices are used to define objects through the Mesh Class and what color they should be.
    Use the `vert.xyz` or `vert.rgb` or variants like `vert.zxy` and `vert.xyrg` to use the data as a numpy array in the order of the attributes.
    Use the `vert.coords` or `vert.color` to get the just the positional or color data as a numpy array.

    ---

    ### Notes

    All values are stored a numpy float32 which hold 32 bits or 4 bytes of data. This is helpful to know the exact size for createing vertex buffers.
    """

    variables = 'xyzrgb'
    """All the variable a Vertex should hold, like __dict__ but as string"""

    one = np.float32(1.0)
    """1.0 as a numpy float32"""
    zero = np.float32(0.0)
    """0.0 as a numpy float32"""

    def __init__(self, *args, default : np.float32 = zero, **kwargs):
        """
        Create a vertex with 3d coordinates and rgb colors.
        Can pass a Squence like object or a numpy array as the input parmaters as well.

        Args:
            - x,y,z,r,g,b : np.float32 values in order, pass as many values as needed the rest will be set to 0.0
            if one value is passed it will be used for all 3d coordinates and color will be set to 0.0

        Keyword Args:
            - x,y,z,r,g,b : np.float32 values in any order, overrides already set values by the args
            - default : np.float32 value to use if no value is passed
        """

        # If the input is a sequence take the sequence as the args
        if isinstance(args[0], (Sequence, np.ndarray)):
            args = args[0]

        args_length = len(args)

        # If one args is passed set it to only the coordinates
        if args_length == 1:
            args = [args[0]]*3
            args_length = len(args)

        # Make sure the default is a numpy float32
        default = np.float32(default)

        # Set x,y,z values if the args exist else set them to 0
        self.x : np.float32 = np.float32(args[0]) if args_length >= 1 else default
        """X postion as a float"""
        self.y : np.float32 = np.float32(args[1]) if args_length >= 2 else default
        """Y postion as a float"""
        self.z : np.float32 = np.float32(args[2]) if args_length >= 3 else default
        """Z postion as a flo  at"""

        # Set r,g,b values if the args exists else set them to 0
        self.r : np.float32 = np.float32(args[3]) if args_length >= 4 else default
        """Red value as a float"""
        self.g : np.float32 = np.float32(args[4]) if args_length >= 5 else default
        """Green value as a float"""
        self.b : np.float32 = np.float32(args[5]) if args_length >= 6 else default
        """Blue value as a float"""

        # Use keyword args to override the values
        for key, value in kwargs.items():
            if key in self.variables:
                self.__dict__[key] = np.float32(value)
            else:
                raise AttributeError(key)

    def copy(self):
        """Retuns a copy of the vertex"""
        return Vertex(self.x, self.y, self.z, self.r, self.g, self.b)

    def magnitude(self):
        """Returns the magnitude of the vertex"""
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def brightness(self):
        """Returns the brightness of the vertex"""
        return np.sqrt(self.r**2 + self.g**2 + self.b**2)

    def normalize(self):
        """Normalizes the vertex to a unit vector"""
        mag = self.magnitude()
        if mag != 0.0:
            self.x /= mag
            self.y /= mag
            self.z /= mag

    def normalize_color(self):
        """Normalize the color to a unit vector"""
        mag = self.brightness()
        if mag != 0.0:
            self.r /= mag
            self.g /= mag
            self.b /= mag

    def __getattr__(self, items : str):
        """Lets us retrive any values in any order as a numpy array"""
        if items == 'coords':
            return np.array([self.x, self.y, self.z], dtype=np.float32)
        elif items == 'color':
            return np.array([self.r, self.g, self.b], dtype=np.float32)
        else:
            # Then its something like xyz, or xy or yzr - in short any combination of x y z / r g b
            attributes = np.zeros(len(items), dtype=np.float32)
            for i, item in enumerate(items):
                if item in self.variables:
                    attributes[i] = self.__dict__[item]
                else:
                    raise AttributeError(item)
            return attributes

    def _set_values(self, items : str, inp):
        """For internal use - assign values directly with "vert.xyz = (0.1, 0.2, 0.3)" instead"""
        if isinstance(inp, (Sequence, np.ndarray)):
            # the input is a sequence
            for i, item in enumerate(items):
                if i < len(inp) and item in self.variables:
                    self.__dict__[item] = np.float32(inp[i])
        else:
            # The input is a single value
            for i, item in enumerate(items):
                if item in self.variables:
                    self.__dict__[item] = np.float32(inp)

    def __setattr__(self, items : str, inp):
        """Set values of the vertex. For example `[vert.xyz | vert.x | vert.rxyb] = ... ` are all valid"""
        # Set some aliases
        if items == 'coords':
            self._set_values('xyz', inp)
        elif items == 'color':
            self._set_values('rgb', inp)
        else:
            # Is it a list of inputs like xyz, or xy or yzr? - in short any combination of x y z / r g b 
            self._set_values(items, inp)

    # create math methods for the vertex class
    def __add__(self, other):
        """Add other to self only considering positional data"""
        if isinstance(other, Vertex):
            return Vertex(self.x + other.x, self.y + other.y, self.z + other.z, self.r, self.g, self.b)
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex and call again
            vert2 = Vertex(other)
            return self.__add__(vert2)
        else:
            return Vertex(self.x + other, self.y + other, self.z + other, self.r, self.g, self.b)
    
    def __radd__(self, other):
        """Add other to self only considering positional data"""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract other from self only considering positional data"""
        if isinstance(other, Vertex):
            return Vertex(self.x - other.x, self.y - other.y, self.z - other.z, self.r, self.g, self.b)
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex and call again
            vert2 = Vertex(other)
            return self.__sub__(vert2)
        else:
            return Vertex(self.x - other, self.y - other, self.z - other, self.r, self.g, self.b)

    def __rsub__(self, other):
        """Subtract other from self only considering positional data"""
        return self.__sub__(other)

    def __mul__(self, other):
        """Multiply self by other only considering positional data"""
        if isinstance(other, Vertex):
            return Vertex(self.x * other.x, self.y * other.y, self.z * other.z, self.r, self.g, self.b)
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex and call again
            vert2 = Vertex(other, default=1.0)
            return self.__mul__(vert2)
        else:
            return Vertex(self.x * other, self.y * other, self.z * other, self.r, self.g, self.b)

    def __rmul__(self, other):
        """Multiply self by other only considering positional data"""
        return self.__mul__(other)

    def __div__(self, other):
        """Divide self by other only considering positional data"""
        if isinstance(other, Vertex):
            return Vertex(self.x / other.x, self.y / other.y, self.z / other.z, self.r, self.g, self.b)
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex and call again
            vert2 = Vertex(other, default=1.0)
            return self.__div__(vert2)
        else:
            return Vertex(self.x / other, self.y / other, self.z / other, self.r, self.g, self.b)

    def __rdiv__(self, other):
        """Divide self by other only considering positional data"""
        return self.__div__(other)

    # true div use div for now
    def __truediv__(self, other):
        """Divide self by other only considering positional data"""
        return self.__div__(other)

    def __rtruediv__(self, other):
        """Divide self by other only considering positional data"""
        return self.__rdiv__(other)


    # Define comparison operators
    def __eq__(self, other):
        """Equality operator for only positional data"""
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex call again
            vert2 = Vertex(other)
            return self.__eq__(vert2)
        else:
            return self.x == other and self.y == other and self.z == other

    # Less then and greater then operators based on magnitude
    def __lt__(self, other):
        """Less than operator for only positional data"""
        if isinstance(other, Vertex):
            return self.magnitude() < other.magnitude()
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex call again
            vert2 = Vertex(other)
            return self.__lt__(vert2)
        else:
            return self.magnitude() < other

    def __gt__(self, other):
        """Greater than operator for only positional data"""
        if isinstance(other, Vertex):
            return self.magnitude() > other.magnitude()
        elif isinstance(other, (Sequence, np.ndarray)):
            # Convert other to vertex call again
            vert2 = Vertex(other)
            return self.__gt__(vert2)
        else:
            return self.magnitude() > other

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __repr__(self):
        return f'Vertex({self.x}, {self.y}, {self.z}, {self.r}, {self.g}, {self.b})'

    # TODO add __str__