import pygame
from pygame.locals import *
from pygame import Vector3

from sys import *
from OpenGL.GL import *

from game.world.world import World
from rendering.shaders.shader import Shader
from rendering.cameras.camera3d import Camera3D

def main():
	pygame.init ()
	screen = pygame.display.set_mode ((800,600), pygame.OPENGL|pygame.DOUBLEBUF, 24)
	glViewport (0, 0, 800, 600)
	glClearColor (0.0, 0.0, 0.0, 1.0)
	glEnableClientState (GL_VERTEX_ARRAY)

	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)

	# Fix this
	glVertexAttribPointer(0, 3, GL_FLOAT, False, GLsizei(9 * 64), *GLvoidp(0));
	glEnableVertexAttribArray(0);

	glVertexAttribPointer(1, 3, GL_FLOAT, False, GLsizei(9 * 64), *GLvoidp(3 * 64));
	glEnableVertexAttribArray(1);

	glVertexAttribPointer(2, 3, GL_FLOAT, False, GLsizei(9 * 64), *GLvoidp(6 * 64));
	glEnableVertexAttribArray(2);

	world = World()

	shader = Shader("./assets/shaders/main")

	camera = Camera3D(90, 800/600, Vector3(0, 0, 0), Vector3(0, 0, 0))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				print("Refreshing")
				world.verts = [
					0.0, 0.5, 0.0, 1, 1, 1, 0, 1, 0,
					-0.5, -0.5, 0.0, 1, 0, 1, 0, 1, 0,
					0.5, -0.5, 0.0, 0, 1, 1, 0, 1, 0
				]
				world.refresh()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glBindBuffer(GL_ARRAY_BUFFER, vbo)
		glVertexPointer(3, GL_FLOAT, 0, None)
		
		world.render()

		shader.use()

		shader.setMatrix4x4("projection", camera.getProjectionMatrix())
		shader.setMatrix4x4("view", camera.getViewMatrix())

		glDrawArrays (GL_TRIANGLES, 0, 3)
		
		pygame.display.flip()
		pygame.time.wait(10)

main()