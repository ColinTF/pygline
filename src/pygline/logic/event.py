from dataclasses import dataclass
from pygline.locals import *

import glfw


@dataclass
class Event:
    """Class to pass event info around"""

    type: int

@dataclass
class KeyEvent(Event):
    """Contains the key and the action"""

    key : int
    action : int
    type : int = KEY_EVENT

@dataclass
class MouseEvent(Event):
    """Contains the button and the action"""

    button : int
    action : int
    type : int = MOUSE_EVENT


class Eventhandler:
    """Handles events and calls functions based on type"""

    def __init__(self):

        # setup call backs
        glfw.set_key_callback(self.window, self.key_callback)
        glfw.set_cursor_pos_callback(self.window, self.cursor_callback)


        self.listeners = {}

    def key_callback(self, window : glfw._GLFWwindow, key : int, scancode : int, action : int, mods : int):
        pass

    def cursor_callback(self, window : glfw._GLFWwindow, xpos : float, ypos : float):
        pass
