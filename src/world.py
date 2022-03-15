from OpenGL.GL import *
from ctypes import *

class World:
	def __init__(self):
		self.mustRender = True
		self.verts = [0]

	def refresh(self):
		self.mustRender = True

	def render(self):
		if (self.mustRender):
			glBufferData(GL_ARRAY_BUFFER, len(self.verts)*4, (c_float*len(self.verts))(*self.verts), GL_STATIC_DRAW)
			self.mustRender = False
