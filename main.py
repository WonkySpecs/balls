import pygame
from pygame.locals import *
import random
import os

from spawner import initial_balls, Spawner
import screen_painter
from ball import Ball
from game_state import GameState
from physics import update_ball, handle_wall_collision

#Set window position on screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

balls = initial_balls(SCREEN_WIDTH, SCREEN_HEIGHT)
grav_balls = []

game_state = GameState()
object_handler = Spawner()
painter = screen_painter.ScreenPainter()
painter.ball_painting_algorithm = screen_painter.speed

while game_state.running:
	game_state.handle_inputs(pygame.event.get())

	object_handler.update(game_state.get_click_spawn_behaviour())
	if pygame.mouse.get_pressed()[0]:
		object_handler.handle_action(game_state.get_click_action(), balls, grav_balls)

	if not game_state.paused:
		balls_to_delete = []
		for ball in balls:
			update_ball(ball, grav_balls)
			handle_wall_collision(ball, game_state.get_wall_action(), SCREEN_WIDTH, SCREEN_HEIGHT)
			if abs(ball.x - SCREEN_WIDTH) > SCREEN_WIDTH or abs(ball.y - SCREEN_HEIGHT) > SCREEN_HEIGHT:
				balls_to_delete.append(ball)

		Spawner.delete(balls_to_delete, balls)

	painter.paint(screen, balls, grav_balls, game_state.get_ball_colour())

	pygame.display.flip()

