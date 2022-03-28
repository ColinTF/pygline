"""
This file stores class templates for convience
"""

class SomeExampleClass:
    """
    # SomeExampleClass

    This class demonstrates how doc strings should be written for this project.
    It also acts as a template

    Attributes:
        - `attribute1` : `int` - stores an int

    Methods:
        - `print` -> `None` - prints `attribute1`

    ---

    ## Usage

    Stores an `int` that can be printed

    ---

    ## Notes

    None
    
    """

    def __init__(self, var1 : int):
        """

        Create SomeClass

        Args:
            - `var1` : `int` - the value to  be assigned to `attribute1`
        
        """

        self.attribute1 = var1

    def print(self):
        """
        
        Prints `attribute1`

        Args:
            - None

        Returns:
            - None
        
        """

        print(self.attribute1)