Module pygline.graphics.shader
==============================

Classes
-------

`ShaderProgram(shader_src: str, src: str)`
:   Stores shader data and the compiled shader
    
    A shader tells the game engine how to handle vertices and colors when displaying them
    
    Create a shader from the passed shader files
    
    This handles the conversion from the file to the actual shader
    
    Loads the shader data from the set file paths
    
    To compile the shader from the data use compile()
    
    Args:
        - shader_src: path to shader folder
        - vert_src: name of the vertex shader as a string
        - frag_src: name of the fragment shader as a string

    ### Methods

    `delete(self)`
    :   Deletes the shader