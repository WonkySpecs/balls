from screen_painter import Colour
from spawner import NewObject

class Modes:
	def __init__(self):
		self.click_spawns = NewObject.INITIAL
		self.ball_colour = Colour.INITIAL
		self.

	def set_from_handled_inputs(self, inputs):
		for mode_to_toggle_to in inputs:
			if isinstance(mode_to_toggle_to, Colour):
				self.ball_colour = mode_to_toggle_to
			elif isinstance(mode_to_toggle_to, NewObject):
				self.click_spawns = mode_to_toggle_to
			else:
				raise Exception("Invalid mode_to_toggle_to " + mode_to_toggle_to + " passed to modes.set_from_handled_inputs()")