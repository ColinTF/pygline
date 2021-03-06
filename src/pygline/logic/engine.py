"""
Welcome to gamegine:

Gamegine is the current working and tempory name for a project by Colin Finnie.
It purpose is to create a system for rapidly prototyping games or just creating simple games.

My current plan is to use the game engine to develop learning enviornments for AI like the open-ai gym.

For now this project mostly functions as a way to learn opengl and improve my python skills.

Thanks for checking it out!
"""

from typing import Callable
import glfw
from OpenGL.GL import *

from pygline.graphics.rendpl import *
from pygline.logic.scene import Scene

from pygline.logic.event import *


import os

# Lets write our class to handle opengl with glfw
class Game:
    """
    This class manages the whole game for us. 
    
    We can use it to: 
        - init glfw and create our window
        - open files to use (textures, shaders)
        - save and load scenes
    """

    def __init__(self, name: str, size: tuple[int, int], src_path : str):

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
            raise Exception("Cant initilize glfw")
        else:

            # Hints to glfw
            # glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE);
            # glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE);
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
                glClearColor(0.07, 0.13, 0.17, 1.0)

                # Setup our event handler
                self.event_handler = EventHandler(self.window)
                self.event_handler.add_event_listener(KEY_EVENT, self.global_key_input)

                # Define all other variables
                self.scene = None

                # Create our variables for time managment
                self.time = glfw.get_time()
                self.last_time = self.time
                self.delta_time = self.time - self.last_time

                # Set the resources paths and subpaths to here
                self.set_resource_dir(src_path)

                self.rendpl = RenderPipeline(self.resource_path)

    def global_key_input(self, event : KeyEvent):
        """Callback function to handle global keyboard events that should always be checked"""

        # Handle window closing this should take priority at all times
        if event.key == glfw.KEY_ESCAPE and event.action == glfw.PRESS:
                glfw.set_window_should_close(self.window, GL_TRUE)


    def add_event_listener(self, type, function : Callable, key=None):
        """Tell the engine to call a function and pass the event when an event is triggerd"""
        pass

    def set_resource_dir(self, path : str):
        """Set the path to look for game resources"""
        self.resource_path = path


    def set_scene(self, scene: Scene):
        """Sets the active scene"""
        # Clear the event handler and populate it with everything in the new scene
        self.event_handler.reset()
        self.event_handler.add_event_listener(KEY_EVENT, self.global_key_input)

        self.scene = scene

        for object in self.scene.get_objects():
            key_listener = getattr(object, 'on_key_event', None)
            if callable(key_listener):
                self.event_handler.add_event_listener(KEY_EVENT, key_listener)


    def start_game_loop(self):
        """
        Starts the game loop

        The game loop will only end when the "window_should_close()" as defined by glfw or another exit condition is met
        """

        glClearColor(0.07, 0.13, 0.17, 1.0)

        while not glfw.window_should_close(self.window):

            # Update variables for time managment
            self.time = glfw.get_time()
            self.delta_time = self.time - self.last_time
            self.last_time = self.time
            
            # Update current scene with delta time
            if not not self.scene:
                self.scene.update(self.delta_time)

            self.rendpl.render(self.scene.vertices, self.scene.indices)

            # Swap buffers to display
            glfw.swap_buffers(self.window)

            # Receive inputs
            glfw.poll_events()

    def end(self):
        """Kills the game window and ends glfw"""
        # Print to console that the game ended
        print(f"Ended game at time: {self.time} s")
        self.rendpl.end()
        glfw.destroy_window(self.window)
        glfw.terminate()
