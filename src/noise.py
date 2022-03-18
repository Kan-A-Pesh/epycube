from perlin_noise import PerlinNoise

class Noise:

	def __init__(self):
		self.noise = PerlinNoise(octaves=10, seed=1)
	
	def get_block_height(self, x, z) -> float:
		value = self.noise([x/100.0, z/100.0])
		return value * 128.0