Module pygline.logic.scene
==========================

Classes
-------

`Scene()`
:   Scenes contain objects that interact with eachother
    
    Load a scene in with the game manager to use it
    
    Scenes are populated with objects and the objects are sorted using a heiracy of dictionaries
    Therefore, it also contains the list of vertices for the game to tell the render pipeline to render

    ### Methods

    `add_group(self, name)`
    :

    `add_object(self, object, dest_group)`
    :

    `get_objects(self, names=[], tags=[], groups=[], op='and', get='object')`
    :

    `merge_group(self, src_group, dest_group='default')`
    :

    `move_object(self, object, dest_group)`
    :

    `rm_group(self, name)`
    :

    `rm_objects(self, objects, announce=False)`
    :

    `update(self, delta_time)`
    :