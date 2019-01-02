import pygame
from pygame.locals import *

from spawner import NewObject
from screen_painter import Colour

class GameState:
	def __init__(self):
		self.running = True
		self.paused = False
		self.click_spawns = NewObject.INITIAL

	def handle_inputs(self, events):
		modes_to_set = []
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_q:
					self.running = False
				elif event.key == K_SPACE:
					self.paused = False if self.paused else True

				if event.key == K_v:
					modes_to_set.append(NewObject.BALL)
				elif event.key == K_f:
					modes_to_set.append(NewObject.GRAV_BALL)
				elif event.key == K_r:
					modes_to_set.append(Colour.RED)
				elif event.key == K_g:
					modes_to_set.append(Colour.GREEN)
				elif event.key == K_b:
					modes_to_set.append(Colour.BLUE)
				elif event.key == K_t:
					modes_to_set.append(Colour.GREY)

			elif event.type == QUIT:
				self.running = False
		return modes_to_set
