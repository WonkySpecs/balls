import pygame
import random
from ball import Ball

def initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT):
	MAX_RADIUS = 25
	return [Ball(random.randint(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS), random.randint(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS), random.randint(2, MAX_RADIUS)) for i in range(10)]

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
