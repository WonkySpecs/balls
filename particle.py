class Particle:
	def __init__(self, x = 0, y = 0, m = 1):
		self.x = x
		self.y = y
		self.m = m
		self.x_vel = 0
		self.y_vel = 0

	def update_pos():
		self.x += self.x_vel
		self.y += self.y_vel

	def udpate_vel(x_f, y_f):
		self.x_vel += x_f / self.m
		self.y_vel += y_f / self.m		

	def update(self, x_force, y_force):
		update_pos()
		update_vel(x_force, y_force)