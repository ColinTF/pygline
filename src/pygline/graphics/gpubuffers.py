from OpenGL.GL import *
from OpenGL.constant import Constant as _C
import numpy as np

class GPU_Buffer:
    """
    A class that lets us control various opengl buffers to minimize boiler plate and simplify code
    """

    def __init__(self, type : _C):
        """Init the buffer with the passed OpenGL buffer type"""
        self.type = type
        self.buffer = glGenBuffers(1)


    def bind(self):
        """Binds the current buffer for use"""
        glBindBuffer(self.type, self.buffer)

    def unbind(self):
        """Unbinds the buffer"""
        glBindBuffer(self.type, 0)

    def delete(self):
        """Deletes the buffer"""
        glDeleteBuffers(1, ctypes.pointer(GLuint(self.buffer)))

class EBO(GPU_Buffer):
    """
    A class that lets us control opengl element buffers to minimize boiler plate and simplify code
    """

    def __init__(self, indices : list[int], size : int, mode : _C):
        """Init the buffer with the passed OpenGL buffer type and bind to it"""
        super().__init__(GL_ELEMENT_ARRAY_BUFFER)
        self.bind()
        glBufferData(self.type, size, indices, mode)


class VBO(GPU_Buffer):
    """
    A class that lets us control opengl vertex buffers to minimize boiler plate and simplify code
    """

    def __init__(self, vertices : list[float], size : int, mode : _C):
        """Init the buffer with the passed OpenGL buffer type  and bind to it"""
        super().__init__(GL_ARRAY_BUFFER)
        self.bind()
        glBufferData(self.type, size, vertices, mode)



class VAO():
    """
    A class that lets us control opengl vertex array buffers to minimize boiler plate and simplify code
    """

    def __init__(self):
        """Init the buffer with the passed OpenGL buffer type"""
        self.buffer = glGenVertexArrays(1)

    def link_attrib(self, vbo : VBO, layout : int, size : int, data_type : type, stride : int, start: int):
        """Temporarily bind the passed vbo and set vertex attribute data at the layout position"""

        vbo.bind()

        glVertexAttribPointer(layout, size, data_type, GL_FALSE, stride, ctypes.c_void_p(start))
        glEnableVertexAttribArray(layout)

        vbo.unbind()

    def bind(self):
        """Binds the current buffer for use"""
        glBindVertexArray(self.buffer)

    def unbind(self):
        """Unbinds the buffer"""
        glBindVertexArray(0)

    def delete(self):
        """Deletes the buffer"""
        # Wack code below dont quite under stand why it had to be this way
        glDeleteVertexArrays(1, ctypes.pointer(GLuint(self.buffer)))

    