

# The imports we need
from typing import Callable
import numpy as np

# Rendering imports
import glfw
from OpenGL.GL import *


# system imports
import os


class Scene:
    """
    Scenes contain objects that interact with eachother

    Load a scene in with the game manager to use it

    Scenes are populated with objects and the objects are sorted using a heiracy of dictionaries
    Therefore, it also contains the list of vertices for the game to tell the render pipeline to render
    
    """


    # Initlize the Scene
    def __init__(self):

        # This will be our container for all objects in the scene, its just a dictionary
        # That will hold other dicts or dicts of dicts etc
        # access it through functions
        self.groups = {'default': {}}

        self.display_vertices = np.array([[]])
        self.display_indices = np.array([])
    

    # Update the whole scene with delta time
    def update(self, delta_time):

        for object in self.get_objects(tags=['updates']):
            object.update(delta_time)
            

    # This next section if for object managment

    # Add an object to a specifc group
    # If the group exists add to it, if it doesnt exist create it with the object in it
    def add_object(self, object, dest_group):
        if dest_group in self.groups:   
            self.groups[dest_group][object._name] = object
        else:
            self.groups[dest_group] = {object._name : object}
        return object

    # Retrive objects by name/tag/group this will be usefull for our other class functions
    # If specified names, ignore all other critera and the op
    # op can be 'and'/'or' it determines if the object must meet 1 or all criteria
    # Depedning on the # of objects/groups in a scene, the critera and operator these could take a while to run
    # get is chooses to return a list of either names/objects
    # TODO Make better search function
    def get_objects(self, names=[], tags=[], groups=[], op='and', get='object'):
        
        objects = []

        return_names = (get == 'name')

        if not not names:
            # Check every object in every group if its name matches a name in names
            for group in self.groups:
                    for object in self.groups[group]:
                        if object in names:
                            objects.append(object if return_names else self.groups[group][object])

        else:

            # If no groups are passed check in all groups
            if not groups:
                groups = self.groups 

            # This line is funny
            use_tags = not not tags

            if op == 'and':
                
                # Loop through only what we need to
                for group in groups:
                    if use_tags:
                        for object in self.groups[group]:
                            if self.groups[group][object].has_tags(tags):
                                objects.append(object if return_names else self.groups[group][object])
                    else:
                        objects.extend([*self.groups[group]] if return_names else [*self.groups[group].values()])
                        

            # If no groups are passed, dont get object by group, but we still need to check every group
            elif op == 'or': 
                # loops through all groups and items and check if they meet a criteria
                for group in self.groups:
                    # The groups is a selected group return all objects inside
                    if group in groups:
                        objects.extend([*self.groups[group]] if return_names else [*self.groups[group].values()])
                    else:
                        if use_tags:
                            for object in self.groups[group]:
                                # Kind of a crazy line of code huh? I think its still readable......
                                if any(self.groups[group][object].has_tags(tag) for tag in tags):
                                    objects.append(object if return_names else self.groups[group][object])

        return objects


    # Remove an object from a specifc group
    # If we cant remove the object raise and error and print to the console
    def rm_objects(self, objects, announce=False):

        objects = [str(x) for x in objects]
        success = False
            
        for object in objects:
            for group in self.groups:
                if object in self.groups[group]:
                        self.groups[group][object].kill(announce)
                        del self.groups[group][object]
                        success = True
                        break  

        if not success:
            print(f"Failed to move '{object}' to '{group}'")
        return success 

     # Move an object between groups, raise an error if it doesnt work
    def move_object(self, object, dest_group):
        object = str(object)
        success = False
        for group in self.groups:

            if object in self.groups[group]:
                item = self.groups[group].pop(object, None)
                self.add_object(item, dest_group)
                success = True
                break  

        if not success:
            print(f"Failed to move '{object}' to '{group}'")
        return success 

        
     # This next section if for group managment
     # Group names, like object names should be unique

    # Add a new group
    def add_group(self, name):
        if name in self.groups:
            print(f"Could not create group: {name}, because it already exists")
        else:
            self.groups[name] = {}

    # Merge src contents into dest then delete src
    # If dest is not specified merge into the default group
    def merge_group(self, src_group, dest_group='default'):
        self.groups[dest_group] |= self.groups[src_group]
        del self.groups[src_group]

    # Remove a group and delete its contents
    # If you dont want to delete its contents consider merge_group
    def rm_group(self, name):
        if name not in self.groups:
            print(f"Could not delete group: {name}, because it does not exist")
        elif name == 'default':
            print("You can not delete the default group")
        else:
            for object in self.groups[name]:
                self.rm_object(object)
            del self.groups[name]


    # Functions that add functionalty to print the class

    def __repr__(self):
        return f"{self.groups}"

    # Loop through every group and prints its objects nicley
    def __str__(self):
        string = f"\nScene Heiracy: \n\n"
        for group in self.groups:
            string += f"|>-{group}\n|>-<|\n"
            for object in self.groups[group]:
                string += f"    |>-{self.groups[group][object]}\tTags: {self.groups[group][object].get_tags()}\n"
            string += f"    |\n"
        return string


