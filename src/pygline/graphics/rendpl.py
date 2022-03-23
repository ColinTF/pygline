from OpenGL.GL import *
from pyrsistent import v

from pygline.graphics.shader import ShaderProgram
from pygline.graphics.gpubuffers import *

NP_32_SIZE = 4

import numpy as np

import os

class RenderPipeline:
    """
    A system for rendering managed by the Game class

    Most users should not need to touch this
    """

    def __init__(self, src_path : str):
        """
        Init the render pipline with the path to the source files
        """

        # Create an empty list of named available shaders
        self.shaders = {}

        self.add_shader(os.path.join(src_path, "shaders"), 'default')
        # self.use_shader('default')

        # Set the bg color #TODO make this changeable
        glClearColor(0.07, 0.13, 0.17, 1.0)

        # Some default settings we want to set
        glEnable(GL_DEPTH_TEST)

    def add_shader(self, path : str, file_name : str):
        self.shaders[file_name] = ShaderProgram(path, file_name)

    def use_shader(self, name):
        glUseProgram(self.shaders[name]._shader)

    def render(self, vertices: np.ndarray, indices: np.ndarray):
        """
        Render the the shapes to the screen

        Args:
            - vertices: list of vertices and their data as a numpy array
            - indices: list of indices associated with the vertices as a numpy array
        """

        # Clear right before we display to minimize flicker I would suspect
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # TODO optimize this process
        self.vao = VAO()
        self.vao.bind()


        self.vbo = VBO(vertices, NP_32_SIZE*len(vertices), GL_DYNAMIC_DRAW)
        self.ebo = EBO(indices, NP_32_SIZE*len(indices), GL_DYNAMIC_DRAW)

        self.vao.link_attrib(self.vbo, 0, 2, GL_FLOAT, NP_32_SIZE*2, 0)
        self.vao.unbind()

        self.vbo.unbind()
        self.ebo.unbind()

        self.use_shader('default')
        self.vao.bind()

        # Finally draw to the screen with the correct method #TODO add new mthods
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    def end(self):
        """Destroy buffers and shaders"""
        self.vao.delete()
        self.vbo.delete()
        self.ebo.delete()
        for shader in self.shaders:
            self.shaders[shader].delete()