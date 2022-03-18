from ursina import *
from face import Face
from noise import Noise

class Chunk:

	chunk_size = 16, 16, 16
	chunk_data = None

	def __init__(self, chunk_pos):
		self.verts = []
		self.tris = []
		self.uvs = []
		self.norms = []
		self.chunk_pos = chunk_pos

		self.generateChunk()

	def generateChunk(self):
		noise = Noise()
		
		x_origin = self.chunk_pos[0] * self.chunk_size[0]
		y_origin = self.chunk_pos[1] * self.chunk_size[1]
		z_origin = self.chunk_pos[2] * self.chunk_size[2]

		self.chunk_data = []

		for x in range(self.chunk_size[0]):
			chunk_side = []

			for z in range(self.chunk_size[2]):
				chunk_line = []
				height = noise.get_block_height(x_origin + x, z_origin + z)
				
				for y in range(self.chunk_size[1]):
					block_id = 0 # Air
					
					if (y_origin + y > height):
						block_id = 1 # Opaque block

					chunk_line.append(block_id)

				chunk_side.append(chunk_line)

			self.chunk_data.append(chunk_side)

	def add_face(self, face: Face):
		self.verts += face.verts
		self.tris += face.tris
		self.uvs += face.uvs
		self.norms += face.norms

	def get_block(self, x, y, z):
		if (x < 0 or y < 0 or z < 0): return 0
		if (x >= self.chunk_size[0] or y >= self.chunk_size[1] or z >= self.chunk_size[2]): return 0

		return self.chunk_data[x][y][z]

	def generateMesh(self):
		self.verts = []
		self.tris = []
		self.uvs = []
		self.norms = []
		
		for x in range(self.chunk_size[0]):
			for y in range(self.chunk_size[1]):
				for z in range(self.chunk_size[2]):
					
					if (self.get_block(x, y, z) == 0):
						continue

					if (self.get_block(x, y+1, z) == 0):
						self.add_face(Face.top((x, y, z), (0,0), (1,1), len(self.verts)))
					if (self.get_block(x, y-1, z) == 0):
						self.add_face(Face.bottom((x, y, z), (0,0), (1,1), len(self.verts)))
					if (self.get_block(x-1, y, z) == 0):
						self.add_face(Face.east((x, y, z), (0,0), (1,1), len(self.verts)))
					if (self.get_block(x+1, y, z) == 0):
						self.add_face(Face.west((x, y, z), (0,0), (1,1), len(self.verts)))
					if (self.get_block(x, y, z+1) == 0):
						self.add_face(Face.north((x, y, z), (0,0), (1,1), len(self.verts)))
					if (self.get_block(x, y, z-1) == 0):
						self.add_face(Face.south((x, y, z), (0,0), (1,1), len(self.verts)))

		return Mesh(vertices=self.verts, triangles=self.tris, uvs=self.uvs, normals=self.norms)