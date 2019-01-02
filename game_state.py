import pygame
from pygame.locals import *

from spawner import NewObject
from screen_painter import Colour

class Modes:
	def __init__(self):
		self.ball_colour = Colour.INITIAL
		self.click_spawn_behaviour = NewObject.INITIAL

	def set(self, value_to_set):
		if isinstance(value_to_set, Colour):
			self.ball_colour = value_to_set
		elif isinstance(value_to_set, NewObject):
			self.click_spawn_behaviour = value_to_set
		else:
			raise Exception("Invalid mode_to_toggle_to " + mode_to_toggle_to + " passed to modes.set_from_handled_inputs()")

class GameState:
	mode_toggle_keys = { K_v : NewObject.BALL,
						 K_f : NewObject.GRAV_BALL,
						 K_r : Colour.RED,
						 K_g : Colour.GREEN,
						 K_b : Colour.BLUE,
						 K_t : Colour.GREY }

	def __init__(self):
		self.modes = Modes()
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
				elif event.key in GameState.mode_toggle_keys.keys():
					self.modes.set(GameState.mode_toggle_keys[event.key])
			elif event.type == QUIT:
				self.running = False

	def get_ball_colour(self):
		return self.modes.ball_colour

	def get_click_spawn_behaviour(self):
		return self.modes.click_spawn_behaviour
