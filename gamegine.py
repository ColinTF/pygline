#The imports we need
import pygame as pg
import numpy as np

# Import some constants we will refer too
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

# Create and event for a key held down
KEYHELD = pg.USEREVENT + 1

GRAVITY = 9.81

# Components are attached to objects to make them unqiue and interact
class component:

    def __init__(self, owner):
        self.owner = owner

    def update(self, delta_time):
        pass

    def kill(self):
        pass

# Allow the object to be re
# ndered to the screen
class renderer(component):

    def __init__(self, owner, output, size=[50, 50], rel_location=np.zeros(2), color=(255,255,255)):
        super().__init__(owner)

        self.surf = pg.Surface(size)
        self.surf.fill(color)

        self.rel_location = rel_location

        self.rect = self.surf.get_rect()

        self.output = output

    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super().update(delta_time)

        self.rect.topleft = self.owner.position + self.rel_location
        self.output.blit(self.surf, self.rect)

# Allow the object to interact with the world
class physics(component):

    def __init__(self, owner, mass=1, friction=0.1, collision=True, gravity=False, passive=False):
        super(physics, self).__init__(owner)

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
        super(physics, self).update(delta_time)

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

    
        
        

# This class will be the parent object to everything that can be seen or does something in the game
# You can attach functionality to the object to make it do intresting stuff like a renderer
class GameObject:

    # The default tags to use
    default_tags = ['updates']

    # Init the object with the time it was made and its name
    # Names should be unique
    def __init__(self, name, pos=np.zeros(2), tags=[]):
        self._name = name
        self._creation_time = pg.time.get_ticks() / 1000.0
        self.tags = []
        self.tags.extend(self.default_tags)

        self.components = []
        self.update_responsibilities = []

        self.position = pos

    # Update all components
    def update(self, delta_time):
        for resposibilty in self.update_responsibilities:
            resposibilty(delta_time)

    # Add components as atrributes and add their update functions to the responsibilties list
    def add_component(self, name, component):
        setattr(self, name, component)
        self.components.append(name)
        self.update_responsibilities.append(component.update)

    def rm_component(self, name, component):
        self.components.remove(name)
        self.component.kill()
        self.update_responsibilities.remove(component.update)
        delattr(self, name)
        


    # These next function allow for tag managment
    # say we want to loop through all our objects and
    # only do something to certain ones
    # might be a good idead to store lists of all objects with a certain tag
    def add_tag(self, tag):
        self.tags.append(tag)

    # Check if a set of tags or tag is assigned
    def has_tags(self, tags):
        if isinstance(tags, list):
            return all(x in self.tags for x in tags)
        else: 
            return tags in self.tags

    def rm_tag(self, tag):
        self.tags.remove(tag)

    def get_tags(self):
        return self.tags

    def kill(self, announce=False):
        if announce:
            print(f"'{self._name}' has been killed and removed")
        for comp in self.components:
            self.components.remove(comp)

    # Functions that add functionalty to print the class
    def __repr__(self):
        return f"{self._name}, {self._creation_time / 1000.0} s"
    def __str__(self):
        return f"{self._name}"

    # Use these for comparing objects and hasing

    def __key(self):
        return (self._name, self._creation_time)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, GameObject):
            return self.__key() == other.__key()
        return NotImplemented



# This class will manage all our objects and updates, will update our scene
class Scene:


    # Initlize the Scene
    def __init__(self):

        # This will be our container for all objects in the scene, its just a dictionary
        # That will hold other dicts or dicts of dicts etc
        # access it through functions
        self.groups = {'default': {}}

        # Init Time and Delta time, althought delta time starts as 0
        self.time = pg.time.get_ticks() / 1000.0
        self.last_time = self.time
        self.delta_time = (self.time - self.last_time)

        # Event handles are a dict with the events for keys and the function for values
        self.event_handles = {}

        # Running is a boolean the update function will return to tell if the scene is still good
        self.running = True

    # Update the whole scene with delta time
    def update(self, events, screen):

        # Clear the screen
        screen.fill((0, 0, 0))

        #Update time and delta time
        self.time = pg.time.get_ticks() / 1000.0
        self.delta_time = (self.time - self.last_time)
        self.last_time = self.time

        # This chunk will handle all our events
        for event in events:

            # Call every function assigned to the event and pass the event
            for function in self.event_handles.get(event.type, []):
                function(event)

            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    self.running = False
                
            elif event.type == QUIT:
                self.running = False

        # Create a keys listener that posts and event of the pressed keys
        keys = pg.key.get_pressed()
        if any(keys):
            pg.event.post(pg.event.Event(KEYHELD, keys=keys))

        for object in self.get_objects(tags=['updates']):
            object.update(self.delta_time)
            

        return self.running

    # Add event handlers
    # Call this and pass an event to listen for and the function it will call
    def add_event_handler(self, event_type, function):
        if event_type in self.event_handles:   
            self.event_handles[event_type].append(function)
        else:
            self.event_handles[event_type] = [function]

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
    # TODO Speed these up cause I bet they are slow
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
