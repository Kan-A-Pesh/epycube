import math
import pygame
from pygame.locals import *
from pygame import Vector3

from sys import *
from OpenGL.GL import *
from ctypes import *

from game.world.world import World
from rendering.shaders.shader import Shader
from rendering.cameras.camera3d import Camera3D

def main():
	pygame.init ()
	screen = pygame.display.set_mode ((800,600), pygame.OPENGL|pygame.DOUBLEBUF, 24)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	getTicksLastFrame = 0

	glViewport (0, 0, 800, 600)
	glClearColor (0.0, 0.0, 0.0, 1.0)
	glEnableClientState (GL_VERTEX_ARRAY)
	glEnable(GL_DEPTH_TEST)

	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)

	# Fix this
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 9 * 4, c_void_p(0))
	glEnableVertexAttribArray(0)

	glVertexAttribPointer(1, 3, GL_FLOAT, False, 9 * 4, c_void_p(3 * 4))
	glEnableVertexAttribArray(1)

	glVertexAttribPointer(2, 3, GL_FLOAT, False, 9 * 4, c_void_p(6 * 4))
	glEnableVertexAttribArray(2)

	world = World()

	shader = Shader("./assets/shaders/main")

	camera = Camera3D(60, 800/600, Vector3(0, 0, 1), Vector3(0, 0, 0))

	world.verts = [
		0.0, 0.5, 0.0, 1, 1, 1, 0, 1, 0,
		-0.5, -0.5, 0.0, 1, 0, 1, 0, 1, 0,
		0.5, -0.5, 0.0, 0, 1, 1, 0, 1, 0
	]
	world.refresh()

	while True:
		dmouse_x, dmouse_y = pygame.mouse.get_pos()[0] - mouse_x, pygame.mouse.get_pos()[1] - mouse_y
		mouse_x, mouse_y = pygame.mouse.get_pos()

		t = pygame.time.get_ticks()
		deltaTime = (t - getTicksLastFrame) / 1000.0
		getTicksLastFrame = t

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					camera.position += camera.getForward() * deltaTime
				if event.key == pygame.K_s:
					camera.position += -camera.getForward() * deltaTime
				if event.key == pygame.K_q:
					camera.position += -camera.getRight() * deltaTime
				if event.key == pygame.K_d:
					camera.position += camera.getRight() * deltaTime
				if event.key == pygame.K_a:
					camera.position += Vector3(0,1,0) * deltaTime
				if event.key == pygame.K_e:
					camera.position += Vector3(0,-1,0) * deltaTime

		camera.rotation.x += dmouse_y * 0.0025
		camera.rotation.z += dmouse_x * 0.0025

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glBindBuffer(GL_ARRAY_BUFFER, vbo)
		glVertexPointer(3, GL_FLOAT, 0, None)

		shader.use()

		world.render(shader)

		shader.setMatrix4x4("projection", camera.getProjectionMatrix())
		shader.setMatrix4x4("view", camera.getViewMatrix())

		glDrawArrays (GL_TRIANGLES, 0, 3)
		
		pygame.display.flip()

main()