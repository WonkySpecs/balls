import pygame
import random
from ball import Ball

MAX_BALLS = 100
NEW_BALL_RATE_LIMIT = 50

class BallSpawner:
	def __init__(self):
		self.time_since_last_ball = NEW_BALL_RATE_LIMIT

	def spawn_ball():
		pos = pygame.mouse.get_pos()
		return Ball(pos[0], pos[1], random.randint(2, 25))

	def add_ball_if_valid(self, balls):
		if  len(balls) < MAX_BALLS and self.time_since_last_ball >= NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball = 0
			balls.append(BallSpawner.spawn_ball())

	def spawn_new_balls(self, new_ball_requested, balls):
		if new_ball_requested:
			self.add_ball_if_valid(balls)

		if self.time_since_last_ball < NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball += 1