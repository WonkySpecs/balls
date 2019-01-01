import pygame
from pygame.locals import *
import random
import os

import new_balls
import screen_painter
from ball import Ball
from game_state import GameState
from physics import update_ball

#Set window position on screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

balls = new_balls.initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT)
grav_balls = [Ball(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 10), Ball(2 * SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3, 10)]

game_state = GameState()
new_ball_handler = new_balls.BallSpawner()
painter = screen_painter.ScreenPainter()
painter.ball_painting_algorithm = screen_painter.speed

while game_state.running:
	game_state.handle_inputs(pygame.event.get())

	if not game_state.paused:
		new_ball_handler.spawn_new_balls(pygame.mouse.get_pressed()[0], balls)

		for ball in balls:
			update_ball(ball, grav_balls)

		painter.paint(screen, balls, grav_balls)

		pygame.display.flip()