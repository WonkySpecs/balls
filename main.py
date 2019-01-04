import pygame
from pygame.locals import *
import random
import os

from spawner import initial_balls, Spawner
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

balls = initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT)
grav_balls = [Ball(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 10), Ball(2 * SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3, 10)]

game_state = GameState()
new_ball_handler = Spawner()
painter = screen_painter.ScreenPainter()
painter.ball_painting_algorithm = screen_painter.speed

while game_state.running:
	game_state.handle_inputs(pygame.event.get())

	new_ball_handler.update(game_state.get_click_spawn_behaviour())
	if pygame.mouse.get_pressed()[0]:
		new_ball_handler.handle_action(game_state.get_click_action(), balls, grav_balls)

	if not game_state.paused:
		for ball in balls:
			update_ball(ball, grav_balls)
			
	painter.paint(screen, balls, grav_balls, game_state.get_ball_colour())

	pygame.display.flip()

