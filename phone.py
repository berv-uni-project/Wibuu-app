import numpy as np
from glumpy import app, gl, glm, gloo, data
from os.path import abspath

vertex = """
	uniform mat4   u_model;         // Model matrix
	uniform mat4   u_view;          // View matrix
	uniform mat4   u_projection;    // Projection matrix
    attribute vec3 a_position;
    varying vec3 v_texcoord;
	varying vec3   v_position;  // Interpolated position (out)
	
    void main()
    {
        gl_Position = u_projection * u_view * u_model * vec4(a_position,1.0);
        v_texcoord = a_position;
		v_position = a_position;
    }
"""

fragment = """
    uniform samplerCube texture;
    varying vec3 v_texcoord;
    void main()
    {
        gl_FragColor = textureCube(texture, v_texcoord);
    }
"""


window = app.Window(width=1024, height=1024,
                    color=(0.30, 0.30, 0.35, 1.00))

@window.event
def on_draw(dt):
	global phi, theta, beta

	window.clear()
	program.draw(gl.GL_QUADS)
	# Rotate cube
	glm.rotate(model, theta, 0, 0, 1)
	glm.rotate(model, phi, 0, 1, 0)
	glm.rotate(model, beta, 1, 0, 0)
	program['u_model'] = model

@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)
	
@window.event
def on_resize(width, height):
    program['u_projection'] = glm.perspective(45.0, width / float(height), 2.0, 100.0)
			 
p = np.array([[+1,+1,+1], [-1,+1,+1], [-1,-1,+1], [+1,-1,+1],
                     [+1,-1,-1], [+1,+1,-1], [-1,+1,-1], [-1,-1,-1]])
n = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0],
                  [-1, 0, 1], [0, -1, 0], [0, 0, -1]])

faces_p = [0, 1, 2, 3,  0, 3, 4, 5,   0, 5, 6, 1,
               1, 6, 7, 2,  7, 4, 3, 2,   4, 7, 6, 5]
faces_n = [0, 0, 0, 0,  1, 1, 1, 1,   2, 2, 2, 2,
		   3, 3, 3, 3,  4, 4, 4, 4,   5, 5, 5, 5]
		   
program = gloo.Program(vertex, fragment)
program["a_position"] = [p[i] for i in faces_p]
# cube['a_normal'] = [face_norm[i] for i in face_normal_idx]

texture = np.zeros((6,1024,1024,3),dtype=np.float32).view(gloo.TextureCube)
texture.interpolation = gl.GL_LINEAR
texture[1] = data.get(abspath("Left_t2.png"))/255.
texture[0] = data.get(abspath("Right_t2.png"))/255.
texture[4] = data.get(abspath("Front_t2.png"))/255.
texture[5] = data.get(abspath("Back_t2.png"))/255.
texture[2] = data.get(abspath("Top_t2.png"))/255.
texture[3] = data.get(abspath("Bottom_t2.png"))/255.

model = np.eye(4,dtype=np.float32)
glm.scale(model, 0.5, 1, 0.1)

program['texture'] = texture
program['u_model'] = model
program['u_view'] = glm.translation(0, 0, -5)
phi = 0.5
theta = 0.1
beta = 0.5

app.run()