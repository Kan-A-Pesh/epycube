import pygame
from pygame.locals import *

from OpenGL.GL import *

from world import World

def main():
	pygame.init ()
	screen = pygame.display.set_mode ((800,600), pygame.OPENGL|pygame.DOUBLEBUF, 24)
	glViewport (0, 0, 800, 600)
	glClearColor (0.0, 0.0, 0.0, 1.0)
	glEnableClientState (GL_VERTEX_ARRAY)

	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)

	world = World()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				world.verts = [
					0.0, 0.5, 0.0,
					-0.5, -0.5, 0.0,
					0.5, -0.5, 0.0
				]
				world.refresh()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glBindBuffer(GL_ARRAY_BUFFER, vbo)
		glVertexPointer(3, GL_FLOAT, 0, None)
		
		world.render()

		glDrawArrays (GL_TRIANGLES, 0, 3)
		
		pygame.display.flip()
		pygame.time.wait(10)

main()