import pygame
from enum import Enum, auto

class Colour(Enum):
	GREY = [0, 1, 2]
	RED = [0]
	GREEN = [1]
	BLUE = [2]

	def initial():
		return Colour.GREY

def one_colour(ball, colour = Colour.RED):
	return colour

def speed(ball, colour = Colour.GREY):
	shade = max(45, round(min(abs((ball.x_vel + ball.y_vel) * 250), 255)))
	return tuple((shade if i in colour.value else 0) for i in range(3))

class ScreenPainter:
	def __init__(self, ball_painting_algorithm = one_colour):
		self.ball_painting_algorithm = ball_painting_algorithm

	def set_painting_algorithms():
		pass

	def paint(self, screen, balls, grav_balls, ball_colour):
		screen.fill((0, 0, 0))

		for ball in balls:
			pygame.draw.circle(screen, self.ball_painting_algorithm(ball, ball_colour), (round(ball.x), round(ball.y)), round(ball.r))

		for grav_ball in grav_balls:
			pygame.draw.circle(screen, (255, 0, 0), (round(grav_ball.x), round(grav_ball.y)), round(grav_ball.r))