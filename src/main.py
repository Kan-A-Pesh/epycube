from ursina import *
from ursina.shaders import lit_with_shadows_shader
from cube import Cube

app = Ursina()
EditorCamera()

cube = Cube()
mesh = cube.generateMesh()

e = Entity(model=mesh, shader=lit_with_shadows_shader, scale=2)

app.run()