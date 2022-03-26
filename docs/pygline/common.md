Module pygline.common
=====================
Common classes and stuctures used through out the whole package

Classes
-------

`Vertex(*args, default: numpy.float32 = 0.0, **kwargs)`
:   # VERTEX
    
    The vertex class is a fundemental, versatille and easy to use class containing positional and color data.
    The data is stored as x,y,z,r,g,b attributes. However the data can be accessed and modified in a variety of ways.
    
    Attributes:
        - `x`,`y`,`z` : `np.float32` - 3d coordinates of vertex
        - `r`,`g`,`b` : `np.float32` - color of vertex
    
    Methods:
        - `copy()` -> `Vertex` - returns a copy of the vertex
        - `get_magnitude()` -> `np.float32` - returns the magnitude of the vertex
        - `get_brightness()` -> `np.float32` - returns the brightness of the vertex
        - `normalize()` -> `None` - normalizes the vertex to a unit vector
    
    ---
    
    ## Usage
    
    Groups of vertices are used to define objects through the Mesh Class and what color they should be.
    Use the `vert.xyz` or `vert.rgb` or variants like `vert.zxy` and `vert.xyrg` to use the data as a numpy array in the order of the attributes.
    Use the `vert.coords` or `vert.color` to get the just the positional or color data as a numpy array. The functionality is designed to be very flexible however,
    the user should be familiar with how the class works. Comparison and math operations only affect the positional data and behave similarly to assignment
    
    Operations:
        - `==` : compares the `x`,`y`,`z` values element wise
        - `<`,`>` : compares the `magnitude()` of the vertex
        - `+`,`-`,`*`,`/` : acts accordingly based on the type of the other object
            - if other is a Vertex : acts element wise
            - if other is a array : acts element wise for values that exist in array
            - if other is a number : acts on all `x`,`y`,`z` values
    
    ---
    
    ## Notes
    
    All values are stored a numpy float32 which hold 32 bits or 4 bytes of data. This is helpful to know the exact size for createing vertex buffers.
    
    Create a vertex with 3d coordinates and rgb colors.
    Can pass a Squence like object or a numpy array as the input parmaters as well.
    
    Args:
        - x,y,z,r,g,b : np.float32 values in order, pass as many values as needed the rest will be set to 0.0
        if one value is passed it will be used for all 3d coordinates and color will be set to 0.0
    
    Keyword Args:
        - x,y,z,r,g,b : np.float32 values in any order, overrides already set values by the args
        - default : np.float32 value to use if no value is passed

    ### Class variables

    `one`
    :   1.0 as a numpy float32

    `variables`
    :   All the variable a Vertex should hold, like __dict__ but as string

    `zero`
    :   0.0 as a numpy float32

    ### Instance variables

    `b`
    :   Blue value as a float

    `g`
    :   Green value as a float

    `r`
    :   Red value as a float

    `x`
    :   X postion as a float

    `y`
    :   Y postion as a float

    `z`
    :   Z postion as a flo  at

    ### Methods

    `copy(self)`
    :   Retuns a copy of the vertex

    `get_brightness(self)`
    :   Returns the brightness of the vertex

    `get_magnitude(self)`
    :   Returns the magnitude of the vertex

    `normalize(self)`
    :   Normalizes the vertex to a unit vector

    `normalize_color(self)`
    :   Normalize the color to a unit vector