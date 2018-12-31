from ball import Ball
import pygame
from pygame.locals import *
import random
import new_balls

def keep_running(events):
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_q:
				return False
		elif event.type == QUIT:
			return False
	return True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_BALL_RADIUS = 25
running = True
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

balls = [Ball(random.randint(MAX_BALL_RADIUS, SCREEN_WIDTH - MAX_BALL_RADIUS), random.randint(MAX_BALL_RADIUS, SCREEN_HEIGHT - MAX_BALL_RADIUS), random.randint(2, MAX_BALL_RADIUS)) for i in range(10)]

new_ball_handler = new_balls.BallSpawner()

while running:
	events = pygame.event.get()
	running = keep_running(events)

	new_ball_handler.spawn_new_balls(pygame.mouse.get_pressed()[0], balls)

	for ball in balls:
		vec_to_centre = (((SCREEN_WIDTH / 2) - ball.x) / 5000, ((SCREEN_HEIGHT / 2) - ball.y) / 5000)
		ball.update(vec_to_centre[0], vec_to_centre[1])

	screen.fill((0,0,0))

	for ball in balls:
		pygame.draw.circle(screen, (255, 255, 255), (round(ball.x), round(ball.y)), round(ball.r))

	pygame.display.flip()