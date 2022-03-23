import numpy as np
from pygline.locals import *
from pygline.common import Vertex

class component:
    """
    Components are attached to objects to make them unqiue and interact

    Components can be defined by the user but built-ins include:
        - Physics
        - Mesh
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
class Mesh(component):
    """
    Stores mesh data in the form of vertices and indices
    """

    def __init__(self, owner, scale : np.ndarray = np.ones(2)/10, rel_location : np.ndarray = np.zeros(2), vertices : np.ndarray = None, primitive_shape : int = PRIMITE_SQUARE):
        """
        Create a mesh component controlled by the parent/owner

        Args:
            - owner: parent to the component
            - scale: relative scale to owner
            - rel_location: relative postion to owner
            - vertices: 2d numpy array of vertices
            - primite_shape: a pre-defined primitive, used if no vertices are given
        """
        super().__init__(owner)

        # By default give the owner a visible tag
        self.owner.add_tag('visible')

        self.rel_location = rel_location
        self.rel_rotation = 0

        
        
        # If no mesh is defined make a primitve
        if not vertices:
            if (primitive_shape == PRIMITE_SQUARE):
                self.vertices = np.array([-1.0, -1.0,
                                          -1.0,  1.0,
                                           1.0, -1.0,
                                           1.0,  1.0], dtype=np.float32)

                self.indices = np.array([0, 1, 2,
                                         1, 2, 3], dtype=np.uint32)

            elif (primitive_shape == PRIMITE_TRIANGLE):
                self.vertices = np.array([ 0.0,  1.0,
                                          -1.0, -1.0,
                                           1.0, -1.0], dtype=np.float32)

                self.indices = np.array([2, 1, 0], dtype=np.uint32)

            elif (primitive_shape == PRIMITE_RIGHT_TRIANGLE):
                self.vertices = np.array([-1.0, -1.0,
                                          -1.0,  1.0,
                                           1.0,  1.0], dtype=np.float32)

                self.indices = np.array([0, 1, 2], dtype=np.uint32)

            else:
                raise Exception("No such primitive exists")

        # Seprate into indidual vertices to apply operations
        for i in range(0, len(self.vertices), 2): 
            self.vertices[i:i + 2] = self.vertices[i:i + 2] * scale + self.rel_location

            



    def normalize_verts():
        """Normalize the whole matrix of vertices in the mesh to have length one"""
        pass



    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super().update(delta_time)

        


# Allow the object to interact with the world
class RigidBody(component):


    def __init__(self, owner, mass=1, friction=0.1, collision=True, gravity=False, passive=False):
        super().__init__(owner)

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