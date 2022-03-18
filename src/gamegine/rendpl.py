from OpenGL.GL import *
from gamegine import components, shader

NP_FLOAT32_SIZE = 4

import numpy as np

class RenderPipeline:
    """
    A system for rendering managed by the Game class

    Most users should not need to touch this
    """

    def __init__(self, shader: shader.Shader):
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

    def set_shader(self, shader: shader.Shader):
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