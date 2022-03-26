Module pygline.objects.components
=================================

Classes
-------

`Mesh(owner, scale: numpy.ndarray = array([0.1, 0.1]), rel_location: numpy.ndarray = array([0., 0.]), vertices: numpy.ndarray = None, primitive_shape: int = 0)`
:   Stores mesh data in the form of vertices and indices
    
    Create a mesh component controlled by the parent/owner
    
    Args:
        - owner: parent to the component
        - scale: relative scale to owner
        - rel_location: relative postion to owner
        - vertices: 2d numpy array of vertices
        - primite_shape: a pre-defined primitive, used if no vertices are given

    ### Ancestors (in MRO)

    * pygline.objects.components.component

    ### Methods

    `normalize_verts()`
    :   Normalize the whole matrix of vertices in the mesh to have length one

    `update(self, delta_time)`
    :

`RigidBody(owner, mass=1, friction=0.1, collision=True, gravity=False, passive=False)`
:   Components are attached to objects to make them unqiue and interact
    
    Components can be defined by the user but built-ins include:
        - Physics
        - Mesh
        - #TODO add more components

    ### Ancestors (in MRO)

    * pygline.objects.components.component

    ### Methods

    `add_force(self, force)`
    :

    `rotate(self, degrees)`
    :

    `set_force(self, force)`
    :

    `update(self, delta_time)`
    :

`component(owner)`
:   Components are attached to objects to make them unqiue and interact
    
    Components can be defined by the user but built-ins include:
        - Physics
        - Mesh
        - #TODO add more components

    ### Descendants

    * pygline.objects.components.Mesh
    * pygline.objects.components.RigidBody

    ### Methods

    `kill(self)`
    :

    `update(self, delta_time)`
    :