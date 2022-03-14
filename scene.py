# The imports we need
from pygame import time, event
from sympy import N


# Our own imports
import gameObjects as obj

# Import some constants we will be using alot for easier code reading
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class group(dict):
    
    def __init__(self, name):
        self.name = name


# This class will manage all our objects and updates will update our scene
# 
# I have yet to figure out what objects will manage physics but this will
# still hold time and delta time variables
# 
class Scene:


    # Initlize the Scene
    def __init__(self):

        # This will be our container for all objects in the scene, its just a dictionary
        # That will hold other dicts or dicts of dicts etc
        # access it through functions
        self.groups = {'default': {}}

        # Init Time and Delta time, althought delta time starts as 0
        self.time = time.get_ticks()
        self.last_time = self.time
        self.delta_time = (self.time - self.last_time) / 1000.0

        # Running is a boolean the update function will return to tell if the scene is still good
        self.running = True

    # Update the whole scene with delta time
    def update(self, events):

        #Update time and delta time
        self.time = time.get_ticks()
        self.delta_time = (self.time - self.last_time) / 1000.0
        self.last_time = self.time

        # This chunk will handle all our events
        for event in events:

            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    self.running = False
                
            elif event.type == QUIT:
                self.running = False

        return self.running

    # This next section if for object managment

    # Add an object to a specifc group
    # If the group exists add to it, if it doesnt exist create it with the object in it
    def add_object(self, object, dest_group):
        if dest_group in self.groups:   
            self.groups[dest_group][object._name] = object
        else:
            self.groups[dest_group] = {object._name : object}

    # Retrive objects by name/tag/group this will be usefull for our other class functions
    # If specified names, ignore all other critera and the op
    # op can be 'and'/'or' it determines if the object must meet 1 or all criteria
    # Depedning on the # of objects/groups in a scene, the critera and operator these could take a while to run
    # TODO Speed these up cause I bet they are slow
    def get_objects(self, names=[], tags=[], groups=[], op='and'):
        
        objects = {}

        if not not names:
            # Check every object in every group if its name matches a name in names
            for group in self.groups:
                    for object in self.groups[group]:
                        if object in names:
                            objects[object] = self.groups[group][object]

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
                                objects[object] = self.groups[group][object]
                    else:
                        objects.update(self.groups[group])

            # If no groups are passed, dont get object by group, but we still need to check every group
            elif op == 'or': 
                # loops through all groups and items and check if they meet a criteria
                for group in self.groups:
                    # The groups is a selected group return all objects inside
                    if group in groups:
                        objects.update(self.groups[group])
                    else:
                        if use_tags:
                            for object in self.groups[group]:
                                # Kind of a crazy line of code huh? I think its still readable......
                                if any(self.groups[group][object].has_tags(tag) for tag in tags):
                                    objects[object] = self.groups[group][object]

        return objects


    # Remove an object from a specifc group
    # If we cant remove the object raise and error and print to the console
    def rm_objects(self, objects, announce=False):
        # success = False
        # del self.get_objects(names=[str(x) for x in objects])
        # print(objects)
        # # for object in objects:
        # #     objects[object].kill(announce)
        # #     success = True

        # # if not success:
        # #     print(f"Failed to delete '{objects}'")
        # # return success

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
