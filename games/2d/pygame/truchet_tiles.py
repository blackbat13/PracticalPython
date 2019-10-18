import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()

width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Truchet Tiles")

screen.fill(WHITE)

side = 50
for x in range(0, width, side):
    for y in range(0, height, side):
        rnd = random.randint(1, 4)
        if rnd == 1:
            pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y), (x, y + side)])
        elif rnd == 2:
            pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y), (x + side, y + side)])
        elif rnd == 3:
            pygame.draw.polygon(screen, BLACK, [(x + side, y), (x + side, y + side), (x, y + side)])
        elif rnd == 4:
            pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y + side), (x, y + side)])
pygame.display.flip()
while True:
    pass
