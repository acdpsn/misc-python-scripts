import time
import sys

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

run = True
while run:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# clear the display
	window.fill(0)

	# draw the scene
	pygame.draw.circle(window, (255, 0, 0), (250, 250), 100)

	# update the display
	pygame.display.flip()
