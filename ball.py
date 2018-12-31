import random
import math

#Simulating mass as proportional to area
def r_to_m(r):
	return math.pi * r**2

class Ball:
	def __init__(self, x = 0, y = 0, r = 1):
		self.x = x
		self.y = y
		self.r = r
		self.m =r_to_m(r)
		self.x_vel = random.uniform(-0.2, 0.2)
		self.y_vel = random.uniform(-0.2, 0.2)

	def update(self, x_force, y_force):
		self.x += self.x_vel
		self.y += self.y_vel

		self.x_vel += x_force / self.m
		self.y_vel += y_force / self.m