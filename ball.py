import random
import math
from particle import Particle

#Simulating mass as proportional to area
def r_to_m(r):
	return math.pi * r**2

class Ball(Particle):
	def __init__(self, x = 0, y = 0, r = 1):
		self.x = x
		self.y = y
		self.r = r
		self.m = r_to_m(r)
		self.x_vel = random.uniform(-0.15, 0.15)
		self.y_vel = random.uniform(-0.15, 0.15)

	def update_pos(self):
		self.x += self.x_vel
		self.y += self.y_vel

	def update_vel(self, x_f, y_f):
		self.x_vel += x_f / self.m
		self.y_vel += y_f / self.m

	def update(self, x_force, y_force):
		self.update_vel(x_force, y_force)
		self.update_pos()

	def vec_to(self, ball):
		return abs(self.x - ball.x), abs(self.y - ball.y)

	def distance_to_squared(self, ball):
		x_d, y_d = self.vec_to(ball)
		return x_d**2 + y_d**2

	def distance_to(self, ball):
		x_d, y_d = self.vec_to(ball)
		return math.sqrt(x_d**2 + y_d**2)