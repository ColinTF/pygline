Module pygline.graphics.gpubuffers
==================================

Classes
-------

`EBO(indices: list[int], size: int, mode: OpenGL.constant.Constant)`
:   A class that lets us control opengl element buffers to minimize boiler plate and simplify code
    
    Init the buffer with the passed OpenGL buffer type and bind to it

    ### Ancestors (in MRO)

    * pygline.graphics.gpubuffers.GPU_Buffer

`GPU_Buffer(type: OpenGL.constant.Constant)`
:   A class that lets us control various opengl buffers to minimize boiler plate and simplify code
    
    Init the buffer with the passed OpenGL buffer type

    ### Descendants

    * pygline.graphics.gpubuffers.EBO
    * pygline.graphics.gpubuffers.VBO

    ### Methods

    `bind(self)`
    :   Binds the current buffer for use

    `delete(self)`
    :   Deletes the buffer

    `unbind(self)`
    :   Unbinds the buffer

`VAO()`
:   A class that lets us control opengl vertex array buffers to minimize boiler plate and simplify code
    
    Init the buffer with the passed OpenGL buffer type

    ### Methods

    `bind(self)`
    :   Binds the current buffer for use

    `delete(self)`
    :   Deletes the buffer

    `link_attrib(self, vbo: pygline.graphics.gpubuffers.VBO, layout: int, size: int, data_type: type, stride: int, start: int)`
    :   Temporarily bind the passed vbo and set vertex attribute data at the layout position

    `unbind(self)`
    :   Unbinds the buffer

`VBO(vertices: list[float], size: int, mode: OpenGL.constant.Constant)`
:   A class that lets us control opengl vertex buffers to minimize boiler plate and simplify code
    
    Init the buffer with the passed OpenGL buffer type  and bind to it

    ### Ancestors (in MRO)

    * pygline.graphics.gpubuffers.GPU_Buffer