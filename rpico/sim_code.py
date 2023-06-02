import time
import sys
import math

import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.Font("Roboto-Regular.ttf", 24)
run = True

while run:
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	# get input
	mouse = pygame.mouse.get_pos()

	# clear the display
	window.fill(0)

	# draw the scene
	pygame.draw.circle(window, (255, 0, 0), (250, 250), 100)
	pygame.draw.arc(window, (0,255,0),(0, 0) + mouse, 0, math.pi * 2)

	# print(pygame.mouse.get_pos())
	# (448, 299)
	# print(pygame.mouse.get_pressed(num_buttons=5))
	# (True, False, True, False, False)

	text_surface, rect = GAME_FONT.render("Hello World!", (255, 255, 255))
	window.blit(text_surface, (40, 250))

	# update the display
	pygame.display.flip()

pygame.quit()
