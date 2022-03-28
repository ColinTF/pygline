from dataclasses import dataclass, field
from typing import Callable
from pygline.locals import *

import glfw


@dataclass(kw_only=True)
class Event:
    """
    Contains an empty event with no data

    Args:
        - time: the time event was created
        - type: the type of event
    
    """

    EMPTY_EVENT = 0
    """Place holder event"""
    KEY_EVENT = 1
    """A key has been triggered"""
    GENERIC_MOUSE_EVENT = 2
    """A mouse event has occurred"""
    CLICK_MOUSE_EVENT = 3
    """The mouse has been clicked"""
    MOVE_MOUSE_EVENT = 4
    """The mouse has been moved"""

    #time : float = field(default_factory=glfw.get_time(), init=False)
    type : int = field(default=EMPTY_EVENT, init=False)

@dataclass(kw_only=True)
class KeyEvent(Event):
    """Contains the key and the action"""

    key : int
    action : int
    type : int = field(default=Event.KEY_EVENT, init=False)

@dataclass(kw_only=True)
class MouseEvent(Event):
    """Contains the button and the action or the postion of the curour or both, mouse event type is mandatory"""

    button : int = None
    action : int = None
    pos : tuple[float, float] = None
    # Default should be generic and be set by user
    type : int = field(default=Event.GENERIC_MOUSE_EVENT)

class EventHandler:
    """Handles events and calls functions based on type"""

    def __init__(self, window : glfw._GLFWwindow):
        """Init with the window the event handler is to be attached to"""

        # setup call backs
        glfw.set_key_callback(window, self.key_callback)
        glfw.set_cursor_pos_callback(window, self.cursor_callback)

        # A dict with keys represrents by type of event contains a list of the functions to call on event triggered
        
        self.listeners : dict[int, list[Callable]] = {Event.EMPTY_EVENT : [], Event.KEY_EVENT : [], Event.MOVE_MOUSE_EVENT : [], Event.CLICK_MOUSE_EVENT : [], Event.GENERIC_MOUSE_EVENT : []} 
        """Dict of lists of function sorted by type of event as the key"""

        self.last_event : Event  = None
        """The most recently generated event"""
        

    def add_event_listener(self, type : int, function : Callable):
        """
        Add and event to the event listener list, 
        the function will be called and passed the event
        when the event of the type is triggered

        Args:
            - type: type of event represented as an integer
            - function: a callable function that will be passed the Event
        """
        self.listeners[type].append(function)

    def rm_event_listener(self, type : int, function : Callable):
        """
        Remove and event to the event listener list, 
        the function will no longer be called and passed the event
        when the event of the type is triggered

        Args:
            - type: type of event represented as an integer
            - function: a callable function that will no longer be passed the Event
        """
        self.listeners[type].remove(function)

    def reset(self):
        """Clears all event listeners"""
        self.listeners : dict[int, list[Callable]] = {Event.EMPTY_EVENT : [], Event.KEY_EVENT : [], Event.MOVE_MOUSE_EVENT : [], Event.CLICK_MOUSE_EVENT : [], Event.GENERIC_MOUSE_EVENT : []} 

    def key_callback(self, window : glfw._GLFWwindow, key : int, scancode : int, action : int, mods : int):
        """Internal key call back function, it is called when GLFW detects a key event"""
        
        # Generate the event
        self.last_event = KeyEvent(key=key, action=action)
        # For each function call it and pass the event
        for func in self.listeners[Event.KEY_EVENT]:
            func(self.last_event)

    def cursor_callback(self, window : glfw._GLFWwindow, xpos : float, ypos : float):
        """Internal cursor call back function, it is called when GLFW detects a cursor event"""
        # Generate the event
        self.last_event = MouseEvent(pos=(xpos, ypos), type=Event.MOVE_MOUSE_EVENT)
        # For each function call it and pass the event
        for func in self.listeners[Event.MOVE_MOUSE_EVENT]:
            func(self.last_event)
