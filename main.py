import pygame
from datetime import datetime

RES = WIDTH, HEIGHT = 1200, 800

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	surface.fill(pygame.Color('black'))
	t = datetime.now()

	time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
	surface.blit(time_render, (120, 150))

	pygame.display.flip()
	clock.tick(20)