import numpy as np
from pygline.locals import *
from pygline.common import Vertex
# from pygline.objects.gameobject import GameObject

class component:
    """
    Components are attached to objects to make them unqiue and interact

    Components can be defined by the user but built-ins include:
        - RigidBody
        - Mesh
        - #TODO add more components
    """

    def __init__(self):
        pass

    def update(self):
        pass

    def kill(self):
        pass

# Allow the object to be re
# rendered to the screen
class Mesh(component):
    """
    # Mesh

    The mesh class acts as a list of `Vertex`s

    Attributes:
        - `owner` : `GameObject` - the owner who controls the mesh
        - `vertices` : `list[Vertex]` - stores all the vertices can be accessed directly or indirectly
        - `indices` : `list[int]` - order of vertices used to describe the mesh
        - `scale` : `np.ndarray` - the xyz scale of the mesh

    Methods:
        - `normalize()` -> `None` - normalizes all the vertices so that the `Vertex` with the longest length has length one

    ---

    ## Usage

    Assign a `Mesh` to an object to make it renderable. `Mesh` can also be used to describe the collision bounds of an object. 
    If applicable, like a base shape, use the same object to descibe both for optimization.

    ---

    ## Notes

    None

    """

    # 2D Shapes
    PRIMITIVE_SQUARE = 0
    """A square using 4 `Vertex`s"""
    PRIMITIVE_TRIANGLE = 1
    """A triangle using 3 `Vertex`s"""
    PRIMITIVE_RIGHT_TRIANGLE = 2
    """A right triangle using 3 `Vertex`"""

    def __init__(self, scale : np.ndarray = np.ones(3)/10, rel_location : np.ndarray = np.zeros(2), vertices : np.ndarray = None, primitive_shape : int = PRIMITIVE_SQUARE):
        """

        Create a new mesh and set the owners tag to visible.

        Args:
            - `owner` : `GameObject` - the owner who controls the mesh
            - `rel_location` : `np.ndarray` - the xyz relative location of the mesh to the owner
            - `scale` : `np.ndarray` - the xyz scale to give the mesh
            - `vertices` : `list[Vertex]` - sets the vertices of the mesh, overides the primitive
            - `primitive_shape` : `int` - the shape of the mesh if no vertices are given

        """

        super().__init__()

        # # By default give the owner a visible tag
        # self.owner.add_tag('visible')

        self.rel_location = rel_location
        self.rel_rotation = 0

        
        
        # If no mesh is defined make a primitve
        if not vertices:
            if (primitive_shape == self.PRIMITIVE_SQUARE):
                                           
                self.vertices = [Vertex(-1.0, -1.0),
                                 Vertex(-1.0,  1.0),
                                 Vertex( 1.0, -1.0),
                                 Vertex( 1.0,  1.0)]

                self.indices = np.array([0, 1, 2,
                                         1, 2, 3], dtype=np.uint32)

            elif (primitive_shape == self.PRIMITIVE_TRIANGLE):
                self.vertices = [Vertex(-1.0, -1.0),
                                 Vertex( 1.0, -1.0),
                                 Vertex( 0.0,  1.0)]

                self.indices = np.array([2, 1, 0], dtype=np.uint32)

            elif (primitive_shape == self.PRIMITIVE_RIGHT_TRIANGLE):
                self.vertices = [Vertex(-1.0, -1.0),
                                 Vertex(-1.0,  1.0),
                                 Vertex( 1.0, -1.0)]

                self.indices = np.array([0, 1, 2], dtype=np.uint32)

            else:
                raise Exception("No such primitive exists")

        # Seprate into indidual vertices to apply operations
        # for i in range(0, len(self.vertices), 2): 
        #     self.vertices[i:i + 2] = self.vertices[i:i + 2] * scale + self.rel_location

            



    def normalize_verts():
        """Normalize the whole matrix of vertices in the mesh to have length one"""
        pass



    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super().update(delta_time)

    def __repr__(self) -> str:
        string = "Mesh(["
        for i in self.indices: 
            string += str(self.vertices[i]) + ", "

        return string + "])"


# Allow the object to interact with the world
class RigidBody(component):


    def __init__(self, mass=1, friction=0.1, collision=True, gravity=False, passive=False):
        super().__init__()

        self.mass = mass

        # # Add appropriate tags to parent
        # if collision:
        #     self.owner.add_tag('collision')
        # if gravity:
        #     self.owner.add_tag('gravity')
        # if passive:
        #     self.owner.add_tag('passive')

        self.friction = friction

        # self.forces = np.array([0, self.mass * GRAVITY]) if self.owner.has_tags(['gravity']) else np.zeros(2)
        self.acceleration = np.zeros(2)
        self.velocity = np.zeros(2)

    # Update the postion using math and delta time
    def update(self, delta_time):
        super().update(delta_time)

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