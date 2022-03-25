# pygline a python and opengl game engine

This package provides a light weight and fast game engine developed specifically for rapid game design and protyping. This project was created by ColinTF and it is currently in the developement phase and now released have been made. 

## Requirments
- [PyOpenGl](https://github.com/mcfletch/pyopengl)
	- The opengl package we use
	- `pip install PyOpenGL PyOpenGL_accelerate` 
	- or download it [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl) and install with `pip install [the name .whl file]`
		- Grab the python 3.10 version of the non accelerate version for your correct system
- [pyGLFW](https://github.com/FlorianRhiem/pyGLFW)
	- The package we use to actually use opengl
	- `pip install glfw`
- [numpy](https://numpy.org/)
	- The package we use for math
	- `pip install numpy`
 
 
 ### Notes
Originally the project was to be a light weight wrapper for pygame. However it was decided to be expanded. Later, during testing, pygame was realized to not fit the needs of the new goals. For example, simple rotations of a square with pygame were very slow and intensive.

