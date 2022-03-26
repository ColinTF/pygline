Module pygline.logic.event
==========================

Classes
-------

`Event()`
:   Contains an empty event with no data
    
    Args:
        - time: the time event was created
        - type: the type of event

    ### Descendants

    * pygline.logic.event.KeyEvent
    * pygline.logic.event.MouseEvent

    ### Class variables

    `type: int`
    :

`EventHandler(window: glfw._GLFWwindow)`
:   Handles events and calls functions based on type
    
    Init with the window the event handler is to be attached to

    ### Instance variables

    `last_event`
    :   The most recently generated event

    `listeners`
    :   Dict of lists of function sorted by type of event as the key

    ### Methods

    `add_event_listener(self, type: int, function: Callable)`
    :   Add and event to the event listener list, 
        the function will be called and passed the event
        when the event of the type is triggered
        
        Args:
            - type: type of event represented as an integer
            - function: a callable function that will be passed the Event

    `cursor_callback(self, window: glfw._GLFWwindow, xpos: float, ypos: float)`
    :   Internal cursor call back function, it is called when GLFW detects a cursor event

    `key_callback(self, window: glfw._GLFWwindow, key: int, scancode: int, action: int, mods: int)`
    :   Internal key call back function, it is called when GLFW detects a key event

    `reset(self)`
    :   Clears all event listeners

    `rm_event_listener(self, type: int, function: Callable)`
    :   Remove and event to the event listener list, 
        the function will no longer be called and passed the event
        when the event of the type is triggered
        
        Args:
            - type: type of event represented as an integer
            - function: a callable function that will no longer be passed the Event

`KeyEvent(*, key: int, action: int)`
:   Contains the key and the action

    ### Ancestors (in MRO)

    * pygline.logic.event.Event

    ### Class variables

    `action: int`
    :

    `key: int`
    :

    `type: int`
    :

`MouseEvent(*, type: int = 2, button: int = None, action: int = None, pos: tuple[float, float] = None)`
:   Contains the button and the action or the postion of the curour or both, mouse event type is mandatory

    ### Ancestors (in MRO)

    * pygline.logic.event.Event

    ### Class variables

    `action: int`
    :

    `button: int`
    :

    `pos: tuple[float, float]`
    :

    `type: int`
    :