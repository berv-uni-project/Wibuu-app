import numpy as np
from glumpy import app, gloo, gl, data
from os.path import abspath

vertex = """
uniform mat4   u_model;         // Model matrix
uniform mat4   u_view;          // View matrix
uniform mat4   u_projection;    // Projection matrix
attribute vec3 a_position;      // Vertex position
attribute vec3 a_texcoord;      // Vertex texture coordinates
varying vec3   v_texcoord;      // Interpolated fragment texture coordinates (out)
void main()
{
    // Assign varying variables
    v_texcoord  = a_texcoord;
    // Final position
    gl_Position = u_projection * u_view * u_model * vec4(a_position,1.0);
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


window = app.Window(width=1024, height=1024)

@window.event
def on_draw(dt):
    window.clear()
    program.draw(gl.GL_TRIANGLES, indices)

@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)

vertices = np.array([[+1,+1,+1], [-1,+1,+1], [-1,-1,+1], [+1,-1,+1],
                     [+1,-1,-1], [+1,+1,-1], [-1,+1,-1], [-1,-1,-1]])
texcoords = np.array([[+1,+1,+1], [-1,+1,+1], [-1,-1,+1], [+1,-1,+1],
                     [+1,-1,-1], [+1,+1,-1], [-1,+1,-1], [-1,-1,-1]])
faces = np.array([vertices[i] for i in [0,1,2,3, 0,3,4,5, 0,5,6,1,
                                        6,7,2,1, 7,4,3,2, 4,7,6,5]])
indices = np.resize(np.array([0,1,2,0,2,3], dtype=np.uint32), 36)
indices += np.repeat(4 * np.arange(6, dtype=np.uint32), 6)
indices = indices.view(gloo.IndexBuffer)
texture = np.zeros((6,1024,1024,3),dtype=np.float32).view(gloo.TextureCube)
texture.interpolation = gl.GL_LINEAR
program = gloo.Program(vertex, fragment, count=24)
program['position'] = faces
program['texcoord'] = faces
program['texture'] = texture

texture[2] = data.get(abspath('Front_t2.png'))/255.
texture[3] = data.get(abspath('Back_t2.png'))/255.
texture[0] = data.get(abspath('Top_t2.png'))/255.
texture[1] = data.get(abspath('Bottom_t2.png'))/255.
texture[4] = data.get(abspath('Left_t2.png'))/255.
texture[5] = data.get(abspath('Right_t2.png'))/255.
app.run()