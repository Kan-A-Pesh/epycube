from ursina import *
from face import Face

class Cube:

	def __init__(self):
		self.verts = []
		self.tris = []
		self.uvs = []
		self.norms = []

		self.add_face(Face.top((0,0,0), (0,0), (1,1), len(self.verts)))
		self.add_face(Face.bottom((0,0,0), (0,0), (1,1), len(self.verts)))
		self.add_face(Face.east((0,0,0), (0,0), (1,1), len(self.verts)))
		self.add_face(Face.west((0,0,0), (0,0), (1,1), len(self.verts)))
		self.add_face(Face.north((0,0,0), (0,0), (1,1), len(self.verts)))
		self.add_face(Face.south((0,0,0), (0,0), (1,1), len(self.verts)))

	def add_face(self, face: Face):
		self.verts += face.verts
		self.tris += face.tris
		self.uvs += face.uvs
		self.norms += face.norms

	def generateMesh(self):
		return Mesh(vertices=self.verts, triangles=self.tris, uvs=self.uvs, normals=self.norms)