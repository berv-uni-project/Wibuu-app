from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
from OpenGL.GLU import *

window = 0  # glut window number
width, height = 800, 600  # window size


def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)  # start drawing a rectangle
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing a rectangle


def draw_circle(x, y, rad):
    posx, posy = x, y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(100):
        glColor3f(1.0, i / 150.0, 0)  # set color to white
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
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


def refresh2d(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.8, 1.0)
    glVertex2f(width, height)
    glVertex2f(0, height)

    glColor3f(0.2, 0.8, 1.0)
    glVertex2f(0, 0)
    glVertex2f(width, 0)
    glEnd()

def colour_tree(x, y, scale):

    glBegin(GL_POLYGON)
    glColor3f(0.4, 0.19, 0.05)

    glVertex2f((x + 175) * scale , (y + 75) * scale)
    glVertex2f((x + 100) * scale, (y + 75) * scale)
    glColor3f(0.4, 0.50, 0.05)
    glVertex2f((x + 100) * scale, (y + 250) * scale)
    glVertex2f((x + 175) * scale, (y + 250) * scale)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.3, 0.0)
    glVertex2f((x + 100) * scale, (y + 250) * scale)
    glVertex2f((x + 0) * scale, (y + 250) * scale)
    glVertex2f((x + 75) * scale, (y + 350) * scale)

    glColor3f(0.0, 0.5, 0.0)
    glVertex2f((x + 25) * scale, (y + 350) * scale)
    glVertex2f((x + 100) * scale, (y + 425) * scale)
    glVertex2f((x + 50) * scale, (y + 425) * scale)

    glColor3f(0.0, 0.7, 0.0)
    glVertex2f((x + 140) * scale, (y + 500) * scale)
    glVertex2f((x + 225) * scale, (y + 425) * scale)
    glVertex2f((x + 175) * scale, (y + 425) * scale)

    glColor3f(0.0, 0.9, 0.0)
    glVertex2f((x + 250) * scale, (y + 350) * scale)
    glVertex2f((x + 200) * scale, (y + 350) * scale)
    glVertex2f((x + 275) * scale, (y + 250) * scale)
    glVertex2f((x + 175) * scale, (y + 250) * scale)
    glEnd()

def draw_tree(x, y):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x + 100, y + 250)
    glVertex2f(x + 175, y + 250)
    glVertex2f(x + 175, y + 75)
    glVertex2f(x + 100, y + 75)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(x + 100, y + 250)
    glVertex2f(x + 0, y + 250)
    glVertex2f(x + 75, y + 350)
    glVertex2f(x + 25, y + 350)
    glVertex2f(x + 100, y + 425)
    glVertex2f(x + 50, y + 425)
    glVertex2f(x + 140, y + 500)
    glVertex2f(x + 225, y + 425)
    glVertex2f(x + 175, y + 425)
    glVertex2f(x + 250, y + 350)
    glVertex2f(x + 200, y + 350)
    glVertex2f(x + 275, y + 250)
    glVertex2f(x + 175, y + 250)
    glEnd()
    colour_tree(x,y, 0.4)

def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    # glColor3f(0.0, 0.0, 1.0)  # set color to blue
    # draw_rect(0, 0, width, height)  # rect at (10, 10) with width 200, height 100
    draw_background()

    colour_tree(50, 0, 0.6)
    colour_tree(800, 0, 0.7)

    draw_circle(width * 0.5, height * 0.9, 50)  # draw circle at (300,300) with radius 50

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
