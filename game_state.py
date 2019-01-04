import pygame
from pygame.locals import *

from spawner import NewObject, ClickAction
from screen_painter import Colour

class Modes:
	def __init__(self):
		self.ball_colour = Colour.initial()
		self.click_spawn_behaviour = NewObject.initial()
		self.click_action = ClickAction.initial()

	def set_ball_colour(self, ball_colour):
		self.ball_colour = ball_colour

	def set_click_spawn_behaviour(self, click_spawn_behaviour):
		self.click_spawn_behaviour = click_spawn_behaviour

	def set_click_action(self, click_action):
		self.click_action = click_action

class GameState:
	mode_toggle_keys = { 
		K_v : lambda modes: Modes.set_click_spawn_behaviour(modes, NewObject.BALL),
		K_f : lambda modes: Modes.set_click_spawn_behaviour(modes, NewObject.GRAV_BALL),
		K_r : lambda modes: Modes.set_ball_colour(modes, Colour.RED),
		K_g : lambda modes: Modes.set_ball_colour(modes, Colour.GREEN),
		K_b : lambda modes: Modes.set_ball_colour(modes, Colour.BLUE),
		K_t : lambda modes: Modes.set_ball_colour(modes, Colour.GREY),
		K_s : lambda modes: Modes.set_click_action(modes, ClickAction.SPAWN),
		K_d : lambda modes: Modes.set_click_action(modes, ClickAction.REMOVE)
	}

	def __init__(self):
		self.modes = Modes()
		self.running = True
		self.paused = False

	def handle_inputs(self, events):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_q:
					self.running = False
				elif event.key == K_SPACE:
					self.paused = False if self.paused else True
				elif event.key in GameState.mode_toggle_keys.keys():
					GameState.mode_toggle_keys[event.key](self.modes)
			elif event.type == QUIT:
				self.running = False

	def get_ball_colour(self):
		return self.modes.ball_colour

	def get_click_spawn_behaviour(self):
		return self.modes.click_spawn_behaviour

	def get_click_action(self):
		return self.modes.click_action