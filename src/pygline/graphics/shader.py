import OpenGL.GL.shaders
from OpenGL.GL import *
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER

import os

class ShaderProgram:
    """
    Stores shader data and the compiled shader

    A shader tells the game engine how to handle vertices and colors when displaying them
    """

    def __init__(self, shader_src: str, vert_src: str, frag_src: str):
        """
        Create a shader from the passed shader files

        This handles the conversion from the file to the actual shader

        Loads the shader data from the set file paths

        To compile the shader from the data use compile()
        
        Args:
            - shader_src: path to shader folder
            - vert_src: name of the vertex shader as a string
            - frag_src: name of the fragment shader as a string
        """

        # For each, open the files and read the contents then close the file
        vert_src = open(os.path.join(shader_src, vert_src), 'r')
        self._vert_data = vert_src.read()
        vert_src.close()

        frag_src = open(os.path.join(shader_src, frag_src), 'r')
        self._frag_data = frag_src.read()
        frag_src.close()

        # Make the vertex and fragment shaders
        self._vert = OpenGL.GL.shaders.compileShader(self._vert_data, GL_VERTEX_SHADER)
        self._frag = OpenGL.GL.shaders.compileShader(self._frag_data, GL_FRAGMENT_SHADER)
        # Make the actual shader
        self._shader = OpenGL.GL.shaders.compileProgram(self._vert, self._frag)
        

    def delete(self):
        """Deletes the shader"""
        glDeleteProgram(self._shader)