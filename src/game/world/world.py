from OpenGL.GL import *
from ctypes import *
from pyrr import *
from numpy import *
from pygame import Vector2, Vector3

class World:
	def __init__(self):
		self.mustRender = True
		self.verts = [0]
		self.position = Vector3(0,0,0)
		self.rotation = Vector3(0,0,0)
		self.scale = Vector3(1,1,1)

	def refresh(self):
		self.mustRender = True

	def render(self, shader):
		if (self.mustRender):
			glBufferData(GL_ARRAY_BUFFER, len(self.verts)*4, (c_float*len(self.verts))(*self.verts), GL_STATIC_DRAW)
			self.mustRender = False
			shader.setMatrix4x4("model", self.getTRSMatrix())

	def getTRSMatrix(self):
		trans = matrix44.create_from_translation(self.position)
		sca = matrix44.create_from_scale(self.scale)
		rot = matrix44.create_from_eulers(self.rotation)

		return matmul(matmul(sca, rot), trans)

