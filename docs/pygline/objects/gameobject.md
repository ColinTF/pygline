Module pygline.objects.gameobject
=================================

Classes
-------

`GameObject(name: str, pos: numpy.ndarray = array([0., 0.]), tags: list[str] = [])`
:   Master class for all objects
    
    All things that move/interact/rendered should be a gameobject. For example, the player, a tree, or even a force field!
    
    Here is what GameObjects can do:
        - have one parent and may have multiple children
        - be organized with tags
        - own components
    
    Warnings:
        - every name MUST be unique. There is built-in methods to do this
    
    Create a blank game object
    
    Args:
        - name: unique string to identify the object
        - pos: starting position as a 2d numpy array
        - tags: list of strings to catagorize the object with

    ### Class variables

    `default_tags`
    :

    ### Methods

    `add_component(self, name: str, component: pygline.objects.components.component)`
    :

    `add_tag(self, tag: str)`
    :

    `get_tags(self) ‑> list[str]`
    :

    `has_tags(self, tags: list[str]) ‑> bool`
    :

    `kill(self, announce: bool = False)`
    :

    `rm_component(self, name: str, component: pygline.objects.components.component)`
    :

    `rm_tag(self, tag: str)`
    :

    `update(self, delta_time)`
    :