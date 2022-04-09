from ursina import *
from ursina.shaders import *
from chunk import Chunk
from player import FirstPersonController
app = Ursina()

# Stopper l'application si la touche échap est préssée
def input(key):
    if key == 'escape':
        app.userExit()

DirectionalLight(y=2, z=3, x=1, shadows=True)

for x in range(-3, 3):
	for y in range(1):
		for z in range(-3, 3):
			chunk_pos = [x,y,z]
			chunk = Chunk(chunk_pos)
			mesh = chunk.generateMesh()
			e = Entity(model=mesh, shader=lit_with_shadows_shader, x=chunk_pos[0]*16, y=chunk_pos[1]*16, z=chunk_pos[2]*16, scale=1)
			e.collider = e.model

player = FirstPersonController(
	y=20,
	origin_y=-.5,
	mouse_sensitivity = Vec2(40, 40),
	height=0.5,
	min_cam_x=-80,
	max_cam_x=80
)

gun = Button(parent=scene, model='cube', color=color.blue, origin_y=-.5, position=(3,0,3), collider='box')
gun.on_click = Sequence(Func(setattr, gun, 'parent', camera), Func(setattr, player, 'gun', gun))

app.run()
