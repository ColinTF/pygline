"""
Welcome to gamegine:

Gamegine is the current working and tempory name for a project by Colin Finnie.
It purpose is to create a system for rapidly prototyping games or just creating simple games.

My current plan is to use the game engine to develop learning enviornments for AI like the open-ai gym.

For now this project mostly functions as a way to learn opengl and improve my python skills.

Thanks for checking it out!
"""

# The imports we need
from typing import Callable
import numpy as np

# Rendering imports
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders

# system imports
import os


NP_FLOAT32_SIZE = 4


class Shader:
    """
    Stores shader data and the compiled shader

    A shader tells the game engine how to handle vertices and colors when displaying them
    """

    def __init__(self, vert_src: str, frag_src: str):
        """
        Create a shader from the passed shader files

        This handles the conversion from the file to the actual shader

        Loads the shader data from the set file paths

        To compile the shader from the data use compile()
        
        Args:
            - vert_src: path to the vertex shader as a string
            - frag_src: path to the fragment shader as a string
        """

        vert_src = open(vert_src, 'r')
        self._vert_data = vert_src.read()
        vert_src.close()

        frag_src = open(frag_src, 'r')
        self._frag_data = frag_src.read()
        frag_src.close()

    def compile(self):
        """Compile the shader for use"""

        self._vert = OpenGL.GL.shaders.compileShader(self._vert_data, GL_VERTEX_SHADER)
        self._frag = OpenGL.GL.shaders.compileShader(self._frag_data, GL_FRAGMENT_SHADER)

        self._shader = OpenGL.GL.shaders.compileProgram(self._vert, self._frag)


class RenderPipeline:
    """
    A system for rendering managed by the Game class

    Most users should not need to touch this
    """

    def __init__(self, shader: Shader):
        """
        Init the render pipline
        """

        # Set the bg color #TODO make this changeable
        glClearColor(0.07, 0.13, 0.17, 1.0)

        # Some default settings we want to set
        glEnable(GL_DEPTH_TEST)

        # Create our buffers
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)

        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)

        # Tell opengl how to read from our buffers
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, NP_FLOAT32_SIZE*6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, NP_FLOAT32_SIZE*6, ctypes.c_void_p(NP_FLOAT32_SIZE*3))

        # Set the shader
        self.set_shader(shader)

    def set_shader(self, shader: Shader):
        """Tell the pipeline which shader to use"""
        glUseProgram(shader._shader)

    def render(self, vertices: np.ndarray, indices: np.ndarray):
        """
        Render the the shapes to the screen

        Args:
            - vertices: list of vertices and their data as a numpy array
            - indices: list of indices associated with the vertices as a numpy array
        """

        # Pass the paramaters into the appropriate buffers
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Clear right before we display to minimize flicker I would suspect
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Finally draw to the screen with the correct method #TODO add new mthods
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

# Lets write our class to handle opengl with glfw

class Game:
    """
    This class manages the whole game for us. 
    
    We can use it to: 
        - init glfw and create our window
        - open files to use (textures, shaders)
        - save and load scenes
    """

    def __init__(self, name: str, size: tuple[int, int]):

        """
        Initialize the game engine
        
        Args:
            - name: name of the window as a string
            - size: width and height of the window as a tuple

        """

        # Define variables set when created
        
        self._name = name
        self._size = size 
        self._width = size[0]
        self._height = size[1]

        # Init glfw and create a window and make sure both tasks complete succesfully
        if not glfw.init():
            raise Exception("Cant initilize Window")
        else:

            glfw.window_hint(glfw.RESIZABLE, glfw.FALSE) # Make the window not resizable
            self.window = glfw.create_window(self._width, self._height, self._name, None, None)

            if not self.window:
                glfw.terminate()
                raise Exception("Could not create glfw window")
            else:

                # Sucsess! Print saying we made a window at the time
                self._game_start_time = glfw.get_time()
                print(f"Created game of size: {self._size} at time: {self._game_start_time}s")

                # Do the rest now

                glfw.set_window_pos(self.window, 20, 40)
                glfw.make_context_current(self.window)
                glViewport(0, 0, self._width, self._height)

                # Define all other variables

                # Create the objects we need
                self.shader = Shader("shaders/vertex.vert", "shaders/fragment.frag")
                self.shader.compile()

                self.render = RenderPipeline(self.shader)
                

    def loop(self):
        """
        Starts the game loop

        The game loop will only end when the "window_should_close()" as defined by glfw or another exit condition is met
        """

        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            
            

            glfw.swap_buffers(self.window)

    def end(self):
        """Kills the game window and ends glfw"""
        # Print to console that the game ended
        print(f"Ended game at time: {self._game_start_time}s")
        glfw.destroy_window(self.window)
        glfw.terminate()

class component:
    """
    Components are attached to objects to make them unqiue and interact

    Components can be defined by the user but built-ins include:
        - Physics
        - Renderer
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
class renderer(component):

    def __init__(self, owner, output, size=[50, 50], rel_location=np.zeros(2), color=(255,255,255)):
        super().__init__(owner)

        self.surf = pg.Surface(size, pg.SRCALPHA)
        self.surf.fill(color)

        self.rel_location = rel_location

        self.rect = self.surf.get_rect()

        self.rotation = 0

        self.output = output

    # Draws the surface to the screen at its position
    def update(self, delta_time):
        super().update(delta_time)

        if self.rotation != self.owner.rotation:
            self.surf = pg.transform.rotate(self.surf, self.owner.rotation-self.rotation)
            self.rect = self.surf.get_rect()
            self.rotation = self.owner.rotation

        self.rect.center = self.owner.position + self.rel_location
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

    # Rotate the object
    def rotate(self, degrees):

        self.owner.rotation += degrees
      


class GameObject:
    """
    Master class for all objects

    All things that move/interact/rendered should be a gameobject. For example, the player, a tree, or even a force field!

    Here is what GameObjects can do:
        - have one parent and may have multiple children
        - be organized with tags
        - own components

    Warnings:
        - every name MUST be unique. There is built-in methods to do this
    """

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
        self.rotation = 0

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


class Scene:
    """
    Scenes contain objects that interact with eachother

    Load a scene in with the game manager to use it

    Scenes are populated with objects and the objects are sorted using a heiracy of dictionaries
    
    """


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


