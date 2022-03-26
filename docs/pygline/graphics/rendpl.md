Module pygline.graphics.rendpl
==============================

Classes
-------

`RenderPipeline(src_path: str)`
:   A system for rendering managed by the Game class
    
    Most users should not need to touch this
    
    Init the render pipline with the path to the source files

    ### Methods

    `add_shader(self, path: str, file_name: str)`
    :

    `end(self)`
    :   Destroy buffers and shaders

    `render(self, vertices: numpy.ndarray, indices: numpy.ndarray)`
    :   Render the the shapes to the screen
        
        Args:
            - vertices: list of vertices and their data as a numpy array
            - indices: list of indices associated with the vertices as a numpy array

    `use_shader(self, name)`
    :