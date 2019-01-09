import pygame
import random
from enum import Enum, auto

from ball import Ball
from force_ball import ForceBall

def initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT):
	MAX_RADIUS = 25
	balls = [Ball(random.randint(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS), random.randint(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS), random.randint(2, MAX_RADIUS)) for i in range(10)]
	for ball in balls:
		ball.x_vel = random.uniform(-0.15, 0.15)
		ball.y_vel = random.uniform(-0.15, 0.15)
	return balls

class NewObject(Enum):
	BALL = auto()
	FORCE_BALL = auto()

	def initial():
		return NewObject.BALL

class ClickAction(Enum):
	SPAWN = auto()
	REMOVE = auto()

	def initial():
		return ClickAction.SPAWN

MAX_BALLS = 100
NEW_BALL_RATE_LIMIT = 50
NEW_FORCE_BALL_RATE_LIMIT = 1000
class Spawner:
	def __init__(self):
		self.time_since_last_ball = NEW_BALL_RATE_LIMIT
		self.time_since_last_force_ball = NEW_FORCE_BALL_RATE_LIMIT
		self.spawns = NewObject.initial()

	def spawn_ball():
		pos = pygame.mouse.get_pos()
		ball = Ball(pos[0], pos[1], random.randint(2, 25))
		ball.x_vel = random.uniform(-0.15, 0.15)
		ball.y_vel = random.uniform(-0.15, 0.15)
		return ball

	def spawn_force_ball(force):
		pos = pygame.mouse.get_pos()
		return ForceBall(pos[0], pos[1], random.randint(2, 25), force)

	def add_ball_if_valid(self, balls):
		if  len(balls) < MAX_BALLS and self.time_since_last_ball >= NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball = 0
			balls.append(Spawner.spawn_ball())

	def add_force_ball_if_valid(self, force_balls, force):
		if  self.time_since_last_force_ball >= NEW_FORCE_BALL_RATE_LIMIT:
			self.time_since_last_force_ball = 0
			force_balls.append(Spawner.spawn_force_ball(force))

	def delete_under_cursor(self, existing):
		mouse_pos = pygame.mouse.get_pos()
		to_remove = [ball for ball in existing if abs(ball.x - mouse_pos[0]) < ball.r and abs(ball.y - mouse_pos[1]) < ball.r]
		Spawner.delete(to_remove, existing)

	def handle_action(self, action, balls, force_balls, force):
		if action == ClickAction.SPAWN:
			if self.spawns == NewObject.BALL:
				self.add_ball_if_valid(balls)
			elif self.spawns == NewObject.FORCE_BALL:
				self.add_force_ball_if_valid(force_balls, force)
			else:
				raise Exception("Spawners 'self' value of " + str(self.spawns) + " is invalid")
		else:
			if self.spawns == NewObject.BALL:
				self.delete_under_cursor(balls)
			elif self.spawns == NewObject.FORCE_BALL:
				self.delete_under_cursor(force_balls)

	def update(self, object_to_spawn):
		self.spawns = object_to_spawn
		if self.time_since_last_ball < NEW_BALL_RATE_LIMIT:
			self.time_since_last_ball += 1
		if self.time_since_last_force_ball < NEW_FORCE_BALL_RATE_LIMIT:
			self.time_since_last_force_ball += 1

	def delete(objects, collection):
		for o in objects:
			if o in collection:
				collection.remove(o)
			else:
				raise Exception("Requested delete on object " + str(o) + " from collection " + str(collection) + " which object was not in")
