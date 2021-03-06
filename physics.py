import math
from enum import Enum, auto

class WallAction(Enum):
	NONE = lambda b, w, h: None
	BOUNCE = lambda b, w, h: wall_bounce(b, w, h)
	WRAP = lambda b, w, h: wrap_around(b, w, h)

	def initial():
		return WallAction.BOUNCE

def calc_grav_force(ball, force_ball):
	f = 0.008 * (ball.m * force_ball.m) / ball.distance_to_squared(force_ball)
	x_d = force_ball.x - ball.x
	y_d = force_ball.y - ball.y
	theta = math.atan(abs(y_d) / abs(x_d))
	x_f = (f * (math.cos(theta))) * (1 if x_d >= 0 else -1)
	y_f = (f * (math.sin(theta))) * (1 if y_d >= 0 else -1)
	return x_f, y_f

def calc_grav_inv_force(ball, force_ball):
	(x_f, y_f) = calc_grav_force(ball, force_ball)
	return -x_f, -y_f

class Force(Enum):
	GRAVITY = calc_grav_force
	GRAVITY_INV = calc_grav_inv_force

	def initial():
		return Force.GRAVITY

def update_ball(ball, force_balls):
	total_x_f = total_y_f = 0
	for force_ball in force_balls:
		x_f, y_f = force_ball.force(ball, force_ball)
		total_x_f += x_f
		total_y_f += y_f

	ball.update(total_x_f, total_y_f)

def handle_wall_collision(ball, wall_action, screen_width, screen_height):
	wall_action(ball, screen_width, screen_height)

def wall_bounce(ball, screen_width, screen_height):
	if (ball.x - ball.r) < 0 or (ball.x + ball.r) > screen_width:
		ball.x_vel *= -1

	if (ball.y - ball.r) < 0 or (ball.y + ball.r) > screen_height:
		ball.y_vel *= -1

def wrap_around(ball, screen_width, screen_height):
	if ball.x < 0:
		ball.x = screen_width

	if ball.x > screen_width:
		ball.x = 0

	if ball.y < 0:
		ball.y = screen_height

	if ball.y > screen_height:
		ball.y = 0