from ursina import *
from ursina.shaders import *
from chunk import Chunk

app = Ursina()
EditorCamera()

DirectionalLight(y=2, z=3, x=1, shadows=True)

for x in range(1):
	for y in range(1):
		for z in range(1):
			chunk_pos = [x,y,z]
			chunk = Chunk(chunk_pos)
			mesh = chunk.generateMesh()
			e = Entity(model=mesh, shader=lit_with_shadows_shader, x=chunk_pos[0]*16, y=chunk_pos[1]*16, z=chunk_pos[2]*16, scale=1)

app.run()