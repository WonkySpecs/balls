from ball import Ball
import pygame
from pygame.locals import *
import random
import new_balls
import screen_painter
import os
import math

def keep_running(events):
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_q:
				return False
		elif event.type == QUIT:
			return False
	return True

def initial_balls():
	MAX_BALL_RADIUS = 25
	return [Ball(random.randint(MAX_BALL_RADIUS, SCREEN_WIDTH - MAX_BALL_RADIUS), random.randint(MAX_BALL_RADIUS, SCREEN_HEIGHT - MAX_BALL_RADIUS), random.randint(2, MAX_BALL_RADIUS)) for i in range(10)]

def calc_grav_force(ball, grav_ball):
	f = 0.008 * (ball.m * grav_ball.m) / ball.distance_to_squared(grav_ball)
	x_d = grav_ball.x - ball.x
	y_d = grav_ball.y - ball.y
	theta = math.atan(abs(y_d) / abs(x_d))
	x_f = (f * (math.cos(theta))) * (1 if x_d >= 0 else -1)
	y_f = (f * (math.sin(theta))) * (1 if y_d >= 0 else -1)
	return x_f, y_f

def update_ball(ball, grav_balls):
	#Pull to centre, further = more force
	#vec_to_centre = (((SCREEN_WIDTH / 2) - ball.x) / 5000, ((SCREEN_HEIGHT / 2) - ball.y) / 5000)

	#Total gravitational pull to grav_balls
	total_x_f = total_y_f = 0
	for grav_ball in grav_balls:
		x_f, y_f = calc_grav_force(ball, grav_ball)
		total_x_f += x_f
		total_y_f += y_f

	ball.update(total_x_f, total_y_f)

#Set window position on screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
balls = initial_balls()
grav_balls = [Ball(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 10), Ball(2 * SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3, 10)]

new_ball_handler = new_balls.BallSpawner()
painter = screen_painter.ScreenPainter()
painter.ball_painting_algorithm = screen_painter.speed

while running:
	events = pygame.event.get()
	running = keep_running(events)

	new_ball_handler.spawn_new_balls(pygame.mouse.get_pressed()[0], balls)

	for ball in balls:
		update_ball(ball, grav_balls)

	painter.paint(screen, balls, grav_balls)

	pygame.display.flip()