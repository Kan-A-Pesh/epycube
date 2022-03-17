from OpenGL.GL import *
from OpenGL.GL.shaders import *
import numpy as np

class Shader:

	def __init__(self, path):
		
		vertex_shader_code = '\n'.join( open( path + ".vert", 'r' ).readlines() )
		vertexShader = glCreateShader(GL_VERTEX_SHADER)
		glShaderSource(vertexShader, vertex_shader_code)
		glCompileShader(vertexShader)

		success = glGetShaderiv(vertexShader, GL_COMPILE_STATUS)
		if not success:
			infoLog = glGetShaderInfoLog(vertexShader)
			print("\n------ Error while compiling vertex shader ------")
			print(infoLog.decode("utf-8"))
			raise Error("Could not compile shader")

		
		fragment_shader_code = '\n'.join( open( path + ".frag", 'r' ).readlines() )
		fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
		glShaderSource(fragmentShader, fragment_shader_code)
		glCompileShader(fragmentShader)

		success = glGetShaderiv(fragmentShader, GL_COMPILE_STATUS)
		if not success:
			infoLog = glGetShaderInfoLog(fragmentShader)
			print("\n------ Error while compiling fragment shader ------")
			print(infoLog.decode("utf-8"))
			raise Error("Could not compile shader")

		self.program = glCreateProgram()
		glAttachShader(self.program, vertexShader)
		glAttachShader(self.program, fragmentShader)
		glLinkProgram(self.program)

		success = glGetProgramiv(self.program, GL_LINK_STATUS)
		if not success:
			infoLog = glGetProgramInfoLog(self.program, 512, None)
			print(infoLog)
			return

		glDeleteShader(vertexShader)
		glDeleteShader(fragmentShader)

	def use(self):
		glUseProgram(self.program)
		
	def setMatrix4x4(self, name, value):
		location = glGetUniformLocation(self.program, name)
		value = value.flatten("C")
		glUniformMatrix4fv(location, 1, False, value)

	def setVector3(self, name, value):
		location = glGetUniformLocation(self.program, name)
		glUniform3fv(location, 1, value)
