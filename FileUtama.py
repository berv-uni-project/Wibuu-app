from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
from OpenGL.GLU import *

window = 0  # glut window number
width, height = 800, 600  # window size

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_circle(x, y, rad):
    posx, posy = x,y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(100):
        glColor3f(1.0, i/150.0, 0)  # set color to white
        cosine = radius * cos(i*2*pi/sides) + posx
        sine = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine,sine)
    glEnd()

def draw_circle_custom(x, y, rad, n):
    posx, posy = x, y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(n):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)
    glVertex2f(0, 0)
    glVertex2f(width, 0)

    glColor3f(0.0, 0.8, 1.0)
    glVertex2f(width, height)
    glVertex2f(0, height)
    glEnd()


def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    #glColor3f(0.0, 0.0, 1.0)  # set color to blue
    #draw_rect(0, 0, width, height)  # rect at (10, 10) with width 200, height 100
    draw_background()

    draw_circle(300, 300, 50) # draw circle at (300,300) with radius 50

    glutSwapBuffers()  # important for double buffering


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
window = glutCreateWindow(b'Pemandangan')  # create window with ti`tle
glutDisplayFunc(draw)  # set draw function callback
glutIdleFunc(draw)  # draw all the time
glutMainLoop()  # start everything