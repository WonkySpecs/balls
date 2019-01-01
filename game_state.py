import pygame
from pygame.locals import *

from spawner import NewObject

class GameState:
	def __init__(self):
		self.running = True
		self.paused = False
		self.click_spawns = NewObject.INITIAL

	def handle_inputs(self, events):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_q:
					self.running = False
				elif event.key == K_SPACE:
					self.paused = False if self.paused else True

				if event.key == K_b:
					self.click_spawns = NewObject.BALL
				if event.key == K_g:
					self.click_spawns = NewObject.GRAV_BALL

			elif event.type == QUIT:
				self.running = False
