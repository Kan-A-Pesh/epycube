from math import cos, sin
from numpy import matrix, ndarray

from pygame import Vector2, Vector3
from pyrr import *
from numpy import *

class Camera3D:

	def __init__(self, fov: float, aspectRatio: float, position: Vector3, rotation: Vector3):
		self.fov = fov
		self.aspectRatio = aspectRatio
		self.position = position
		self.rotation = rotation

	def getForward(self) -> Vector3:
		r = self.rotation
		c = (cos(r.x), cos(r.y))
		s = (sin(r.x), sin(r.y))

		fwd = (-s[0] * abs(c[1]), s[1], -c[0] * abs(c[1]))
		
		return Vector3(fwd)

	def getRight(self) -> Vector3:
		return Vector3.normalize(Vector3.cross(Vector3(0,1,0), -self.getForward()))

	def getUp(self) -> Vector3:
		return Vector3.normalize(Vector3.cross(-self.getForward(), self.getRight()))

	def getProjectionMatrix(self) -> ndarray:
		return matrix44.create_perspective_projection_matrix(self.fov, self.aspectRatio, 0.01, 1000)

	def getViewMatrix(self) -> ndarray:
		trans = matrix44.create_from_translation(self.position)
		rot = matrix44.create_from_eulers(self.rotation)

		return linalg.inv(matmul(rot, trans))