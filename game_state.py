import pygame
from pygame.locals import *

class GameState:
	def __init__(self):
		self.running = True
		self.paused = False

	def handle_inputs(self, events):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_q:
					self.running = False
				elif event.key == K_SPACE:
					self.paused = False if self.paused else True
			elif event.type == QUIT:
				self.running = False
