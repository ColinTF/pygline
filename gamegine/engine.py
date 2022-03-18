"""
Welcome to gamegine:

Gamegine is the current working and tempory name for a project by Colin Finnie.
It purpose is to create a system for rapidly prototyping games or just creating simple games.

My current plan is to use the game engine to develop learning enviornments for AI like the open-ai gym.

For now this project mostly functions as a way to learn opengl and improve my python skills.

Thanks for checking it out!
"""

import glfw
from OpenGL.GL import *
from .rendpl import RenderPipeline
from .shader import Shader

NP_FLOAT32_SIZE = 4
GRAVITY = 9.81

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