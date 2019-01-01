import pygame
from enum import Enum, auto

C_WHITE = (255, 255, 255)
C_BLACK = (0,0,0)

def one_colour(ball, colour = C_WHITE):
	return colour

def speed(ball):
	shade = max(45, round(min(abs((ball.x_vel + ball.y_vel) * 250), 255)))
	return (shade, shade, shade)

class ScreenPainter:
	def __init__(self, ball_painting_algorithm = one_colour):
		self.ball_painting_algorithm = ball_painting_algorithm

	def set_painting_algorithms():
		pass

	def paint(self, screen, balls, grav_balls):
		screen.fill(C_BLACK)

		for ball in balls:
			pygame.draw.circle(screen, self.ball_painting_algorithm(ball), (round(ball.x), round(ball.y)), round(ball.r))

		for grav_ball in grav_balls:
			pygame.draw.circle(screen, (255, 0, 0), (round(grav_ball.x), round(grav_ball.y)), round(grav_ball.r))