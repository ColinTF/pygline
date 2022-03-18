from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

name = "Hello, World"
height = 400
width = 400
rotate = 0
beginx = 0.
beginy = 0.
rotx = 0.
roty = 0.

def display():
     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
     glLoadIdentity()
     gluLookAt(0,0,10,0,0,0,0,1,0)
     glRotatef(roty,0,1,0)
     glRotatef(rotx,1,0,0)
     glCallList(1)
     glutSwapBuffers()
     return

def mouse(button,state,x,y):
     global beginx,beginy,rotate
     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
         rotate = 1
         beginx = x
         beginy = y
     if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
         rotate = 0
     return

def motion(x,y):
     global rotx,roty,beginx,beginy,rotate
     if rotate:
         rotx = rotx + (y - beginy)
         roty = roty + (x - beginx)
         beginx = x
         beginy = y
         glutPostRedisplay()
     return

def keyboard(a,b,c):
     return

glutInit(name)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(height,width)
glutCreateWindow(name)
glClearColor(0., 0., 0., 1.)

# setup display list
glNewList(1, GL_COMPILE)
glPushMatrix()
glTranslatef(0., 1., 0.) #move to where we want to put object
glutSolidSphere(1., 20, 20) # make radius 1 sphere of res 10x10
glPopMatrix()
glPushMatrix()
glTranslatef(0., -1., 0.) #move to where we want to put object
glutSolidSphere(1., 20, 20) # make radius 1 sphere of res 10x10
glPopMatrix()
glEndList()

#setup lighting
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
lightZeroPosition = [10., 4., 10., 1.]
lightZeroColor = [0.8, 1.0, 0.8, 1.0] # greenish
glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
glEnable(GL_LIGHT0)

#setup cameras
glMatrixMode(GL_PROJECTION)
gluPerspective(40., 1., 1., 40.)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
glPushMatrix()

#setup callbacks
glutDisplayFunc(display)
glutMouseFunc(mouse)
glutMotionFunc(motion)
glutKeyboardFunc(keyboard)

glutMainLoop()