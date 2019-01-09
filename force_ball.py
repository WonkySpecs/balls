from ball import Ball
from physics import Force

class ForceBall(Ball):
	def __init__(self, x = 0, y = 0, r = 1, force = Force.GRAVITY_INV):
		super().__init__(x, y, r)
		self.force = force