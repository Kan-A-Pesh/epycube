from OpenGL.GL import *
from OpenGL.GL.shaders import *

class Shader:

	def __init__(self, path):
		
		vertex_shade_code = '\n'.join( open( path + ".vert", 'r' ).readlines() )
		fragment_shader_code = '\n'.join( open( path + ".frag", 'r' ).readlines() )

		self.program = compileProgram(
			compileShader( vertex_shade_code,GL_VERTEX_SHADER),
			compileShader( fragment_shader_code,GL_FRAGMENT_SHADER),)

	def use(self):
		glUseProgram(self.program)
		
	def setMatrix4x4(self, name, value):
		location = glGetUniformLocation(self.program, name)
		glUniformMatrix4fv(location, 1, False, value)

	def setVector3(self, name, value):
		location = glGetUniformLocation(self.program, name)
		glUniform3fv(location, 1, value)
