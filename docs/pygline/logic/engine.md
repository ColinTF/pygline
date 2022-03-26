Module pygline.logic.engine
===========================
Welcome to gamegine:

Gamegine is the current working and tempory name for a project by Colin Finnie.
It purpose is to create a system for rapidly prototyping games or just creating simple games.

My current plan is to use the game engine to develop learning enviornments for AI like the open-ai gym.

For now this project mostly functions as a way to learn opengl and improve my python skills.

Thanks for checking it out!

Classes
-------

`Game(name: str, size: tuple[int, int], src_path: str)`
:   This class manages the whole game for us. 
    
    We can use it to: 
        - init glfw and create our window
        - open files to use (textures, shaders)
        - save and load scenes
    
    Initialize the game engine
    
    Args:
        - name: name of the window as a string
        - size: width and height of the window as a tuple

    ### Methods

    `add_event_listener(self, type, function: Callable, key=None)`
    :   Tell the engine to call a function and pass the event when an event is triggerd

    `end(self)`
    :   Kills the game window and ends glfw

    `global_key_input(self, event: pygline.logic.event.KeyEvent)`
    :   Callback function to handle global keyboard events that should always be checked

    `set_resource_dir(self, path: str)`
    :   Set the path to look for game resources

    `set_scene(self, scene: pygline.logic.scene.Scene)`
    :   Sets the active scene

    `start_game_loop(self)`
    :   Starts the game loop
        
        The game loop will only end when the "window_should_close()" as defined by glfw or another exit condition is met