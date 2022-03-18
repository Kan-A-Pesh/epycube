from ursina import *

app = Ursina()
EditorCamera()

verts = ((0,1,0), (0.5, 0, 0), (-0.5, 0, 0))
tris = (0, 1, 2)
uvs = ((0,1), (0.5, 0), (-0.5, 0))
norms = ((0, 0, -1),)

e = Entity(model=Mesh(vertices=verts, triangles=tris, uvs=uvs, normals=norms), scale=2)

app.run()