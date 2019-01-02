import pygame
import random
from enum import Enum, auto

from ball import Ball

def initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT):
	MAX_RADIUS = 25
	balls = [Ball(random.randint(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS), random.randint(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS), random.randint(2, MAX_RADIUS)) for i in range(10)]
	for ball in balls:
		ball.x_vel = random.uniform(-0.15, 0.15)
		ball.y_vel = random.uniform(-0.15, 0.15)
	return balls

class NewObject(Enum):
	BALL = auto()
	GRAV_BALL = auto()

	def initial():
		return NewObject.BALL

class ClickAction(Enum):
	SPAWN = auto()
	REMOVE = auto()

	def initial():
		return ClickAction.SPAWN

MAX_BALLS = 100
NEW_BALL_RATE_LIMIT = 50
NEW_GRAV_BALL_RATE_LIMIT = 1000
class Spawner:
	def __init__(self):
		self.time_since_last_ball = NEW_BALL_RATE_LIMIT
		self.time_since_last_grav_ball = NEW_GRAV_BALL_RATE_LIMIT
		self.spawns = NewObject.initial()

	def spawn_ball():
		pos = pygame.mouse.get_pos()
		ball = Ball(pos[0], pos[1], random.randint(2, 25))
		ball.x_vel = random.uniform(-0.15, 0.15)
		ball.y_vel = random.uniform(-0.15, 0.15)
		return ball

	def spawn_grav_ball():
		pos = pygame.mouse.get_pos()
		return Ball(pos[0], pos[1], random.randint(2, 25))

	def add_ball_if_valid(self, balls):
		if  len(balls) < MAX_BALLS and self.time_since_last_ball >= NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball = 0
			balls.append(Spawner.spawn_ball())

	def add_grav_ball_if_valid(self, grav_balls):
		if  self.time_since_last_grav_ball >= NEW_GRAV_BALL_RATE_LIMIT:
			self.time_since_last_grav_ball = 0
			grav_balls.append(Spawner.spawn_grav_ball())

	def delete_under_cursor(self, existing):
		mouse_pos = pygame.mouse.get_pos()
		to_remove = [ball for ball in existing if abs(ball.x - mouse_pos[0]) < ball.r and abs(ball.y - mouse_pos[1]) < ball.r]
		for ball in to_remove:
			existing.remove(ball)

	def handle_action(self, action, balls, grav_balls):
		if action == ClickAction.SPAWN:
			if self.spawns == NewObject.BALL:
				self.add_ball_if_valid(balls)
			elif self.spawns == NewObject.GRAV_BALL:
				self.add_grav_ball_if_valid(grav_balls)
			else:
				raise Exception("Spawners 'self' value of " + str(self.spawns) + " is invalid")
		else:
			if self.spawns == NewObject.BALL:
				self.delete_under_cursor(balls)
			elif self.spawns == NewObject.GRAV_BALL:
				self.delete_under_cursor(grav_balls)

	def update(self, object_to_spawn):
		self.spawns = object_to_spawn
		if self.time_since_last_ball < NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball += 1
		if self.time_since_last_grav_ball < NEW_GRAV_BALL_RATE_LIMIT:
			self.time_since_last_grav_ball += 1