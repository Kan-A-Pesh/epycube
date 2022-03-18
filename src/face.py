class Face:
	
	def __init__(self, tris, uvs, norms):
		self.tris = tris
		self.uvs = uvs
		self.norms = norms
		self.verts = []

	@staticmethod
	def get_norms(id):
		return (
			( 0, 1, 0), # Top / y+
			( 0,-1, 0), # Bottom / y-
			(-1, 0, 0), # East / Left / x-
			( 1, 0, 0), # West / Right / x+
			( 0, 0, 1), # North / Forward / z+
			( 0, 0,-1)  # South / Backward / z-
		)[id]

	@staticmethod
	def get_face(id: int, uv_origin: tuple[int, int], uv_size: tuple[int, int], tid: int):
		tris = (tid + 0, tid + 1, tid + 2, tid + 2, tid + 1, tid + 3)
		norms = (Face.get_norms(id),) * 4 # Cuz a face is a 4 vertices
		uvs = (
			((uv_origin[0] + 0)*uv_size[0], (uv_origin[1] + 0)*uv_size[1]), 
			((uv_origin[0] + 1)*uv_size[0], (uv_origin[1] + 0)*uv_size[1]), 
			((uv_origin[0] + 0)*uv_size[0], (uv_origin[1] + 1)*uv_size[1]), 
			((uv_origin[0] + 1)*uv_size[0], (uv_origin[1] + 1)*uv_size[1])
		)

		return Face(tris, uvs, norms)

	@staticmethod
	def top(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # Top / y+
		face = Face.get_face(0, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 0, pos[1] + 1, pos[2] + 0),
			(pos[0] + 1, pos[1] + 1, pos[2] + 0),
			(pos[0] + 0, pos[1] + 1, pos[2] + 1),
			(pos[0] + 1, pos[1] + 1, pos[2] + 1),
		)
		return face

	@staticmethod
	def bottom(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # Bottom / y-
		face = Face.get_face(1, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 0, pos[1] + 0, pos[2] + 0),
			(pos[0] + 0, pos[1] + 0, pos[2] + 1),
			(pos[0] + 1, pos[1] + 0, pos[2] + 0),
			(pos[0] + 1, pos[1] + 0, pos[2] + 1),
		)
		return face

	@staticmethod
	def east(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # East / Left / x-
		face = Face.get_face(2, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 0, pos[1] + 0, pos[2] + 0),
			(pos[0] + 0, pos[1] + 1, pos[2] + 0),
			(pos[0] + 0, pos[1] + 0, pos[2] + 1),
			(pos[0] + 0, pos[1] + 1, pos[2] + 1),
		)
		return face

	@staticmethod
	def west(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # West / Right / x+
		face = Face.get_face(3, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 1, pos[1] + 0, pos[2] + 0),
			(pos[0] + 1, pos[1] + 0, pos[2] + 1),
			(pos[0] + 1, pos[1] + 1, pos[2] + 0),
			(pos[0] + 1, pos[1] + 1, pos[2] + 1),
		)
		return face

	@staticmethod
	def north(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # North / Forward / z+
		face = Face.get_face(4, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 0, pos[1] + 0, pos[2] + 1),
			(pos[0] + 0, pos[1] + 1, pos[2] + 1),
			(pos[0] + 1, pos[1] + 0, pos[2] + 1),
			(pos[0] + 1, pos[1] + 1, pos[2] + 1),
		)
		return face

	@staticmethod
	def south(pos: tuple[int, int, int], uv_origin: tuple[int, int], uv_size: tuple[int, int], tris_index: int): # South / Backward / z-
		face = Face.get_face(5, uv_origin, uv_size, tris_index)
		face.verts = (
			(pos[0] + 0, pos[1] + 0, pos[2] + 0),
			(pos[0] + 1, pos[1] + 0, pos[2] + 0),
			(pos[0] + 0, pos[1] + 1, pos[2] + 0),
			(pos[0] + 1, pos[1] + 1, pos[2] + 0),
		)
		return face