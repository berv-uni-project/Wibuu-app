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

def circle(x, y, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = i*2*(pi/100)
        glVertex2f(x+(cos(angle)*radius),y+(sin(angle)*radius))
    glEnd()

def draw_circle_filled(x, y, rad, n, a, b, c):
    posx, posy = x, y
    sides = 50
    radius = rad
    #glColor4f(a + 0.035, b + 0.025, c + 0.015, 0.4)
    for i in range(n):
        # glColor3f(a + 0.02 * i, b + 0.02 * i, c + 0.02 * i)
        glColor3f(a + 0.035 * i, b + 0.025 * i, c + 0.015 * i)
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)


def draw_circle_custom(x, y, rad, n):
    posx, posy = x, y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(n):
        glColor3f(i / 50.0, i / 10.0, 0)
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
    glColor3f(0.2, 0.8, 1.0)
    glVertex2f(width, height)
    glVertex2f(0, height)

    glColor3f(0.7, 0.8, 1.0)
    glVertex2f(0, 0)
    glVertex2f(width, 0)
    glEnd()

def draw_cloud(x, y, size):
    glColor3f(1.0, 1.0, 1.0)
    circle(x, y, size)
    circle(x + 25, y - 10, size + 10)
    circle(x + 60, y - 7, size + 20)
    circle(x + 100, y - 10, size + 10)

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

def draw_rainbow(x, y, w, step):
    dx, dy = x, y
    up = 0
    n = 1000
    for i in range(n):
        glBegin(GL_QUAD_STRIP)
        glColor3f(1, 0, 0) # Red
        glVertex2f(dx, dy - step)
        glVertex2f(dx + w, dy - step - up)

        glColor3f(1, 0.6, 0) # Orange
        glVertex2f(dx, dy - step * 1.1)
        glVertex2f(dx + w, dy - step * 1.1 - up)

        glColor3f(1, 1, 0) # Yellow
        glVertex2f(dx, dy - step * 1.2)
        glVertex2f(dx + w, dy - step * 1.2 - up)

        glColor3f(0.2, 1, 0) # Green
        glVertex2f(dx, dy - step * 1.3)
        glVertex2f(dx + w, dy - step * 1.4 - up)

        glColor3f(0, 0.6, 1) # Blue
        glVertex2f(dx, dy - step * 1.5)
        glVertex2f(dx + w, dy - step * 1.5 - up)

        glColor3f(0.4, 0.2, 1) # Purple
        glVertex2f(dx, dy - step * 1.6)
        glVertex2f(dx + w, dy - step * 1.6 - up)

        glEnd()

        dx = dx + w
        dy = dy + 0.01 * sin(i * 3.14 / 5.0)
        if (dx < width / 2):
            step = step - 0.045
        else:
            step = step + 0.045

def draw_rainbow2(x, y):
    rad = 500
    n = 16
    glBegin(GL_POLYGON)
    draw_circle_filled(x, y, rad, n, 1, 0, 0)
    draw_circle_filled(x, y-10, rad, n, 1, 0.6, 0)
    draw_circle_filled(x, y-20, rad, n, 1, 1, 0)
    draw_circle_filled(x, y-30, rad, n, 0.2, 1, 0)
    draw_circle_filled(x, y-40, rad, n, 0, 0.6, 1)
    draw_circle_filled(x, y-50, rad, n, 0.4, 0.2, 1)
    glEnd()

    glColor3f(0.2, 0.8, 1) # background
    circle(x, y-60, rad)

def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    # background
    draw_background()

    draw_rainbow(100, 520, 0.5, 50)
    #draw_rainbow2(300, 0)

    # Gunung 1
    draw_circle_custom(200, -100, 300, 18)

    # Gunung 2
    draw_circle_custom(600, -100, 300, 18)

    # pohon 1
    colour_tree(50, 0, 0.6)

    # pohon 2
    colour_tree(800, 0, 0.7)

    # matahari
    draw_circle(width * 0.5, height * 0.9, 50)  # draw circle at (300,300) with radius 50

    draw_cloud(100,450,30)
    draw_cloud(600, 450, 30)

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
