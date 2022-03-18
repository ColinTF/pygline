import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

import os

NP_FLOAT32_SIZE = 4

WIDTH = 800
HEIGHT = 800

def window_resize(window, width, height):
    WIDTH = width
    HEIGHT = height
    glViewport(0, 0, WIDTH, HEIGHT)

vertex_src_file = open("shaders/vertex.vert", "r")
vertex_src = vertex_src_file.read()
vertex_src_file.close()

fragment_src_file = open("shaders/fragment.frag", "r")
fragment_src = fragment_src_file.read()
fragment_src_file.close()


vertices = np.array([   

    -0.5, -0.5,  0.0,  1.0,  0.0,  0.0,
     0.5, -0.5,  0.0,  0.0,  1.0,  0.0,
    -0.5,  0.5,  0.0,  0.0,  0.0,  1.0,
     0.5,  0.5,  0.0,  1.0,  1.0,  1.0,
     0.0, 0.75,  0.0,  1.0,  1.0,  0.0

    ], dtype=np.float32)


indices = np.array([

    0, 1, 2,
    1, 2, 3,
    2, 3, 4

    ], dtype=np.uint32)

if not glfw.init():
    raise Exception("Cant initilize Window")

window = glfw.create_window(WIDTH, HEIGHT, "Test2", None, None)

if not window:
    glfw.terminate()
    raise Exception("Could not create glfw window")

glfw.set_window_pos(window, 200, 100)

glfw.set_window_size_callback(window, window_resize)

glfw.make_context_current(window)

glClearColor(0.07, 0.13, 0.17, 1.0)

glEnable(GL_DEPTH_TEST)

glViewport(0, 0, WIDTH, HEIGHT)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))


VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, NP_FLOAT32_SIZE*6, ctypes.c_void_p(0))


glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, NP_FLOAT32_SIZE*6, ctypes.c_void_p(NP_FLOAT32_SIZE*3))

glUseProgram(shader)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)


    glfw.swap_buffers(window)


glfw.destroy_window(window)
glfw.terminate()