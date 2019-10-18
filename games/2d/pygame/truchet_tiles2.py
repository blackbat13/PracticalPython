import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()

width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Truchet Tiles")

screen.fill(WHITE)
PI = math.pi
side = 100
for x in range(0, width, side-3):
    for y in range(0, height, side-10):
        rnd = random.randint(1, 4)
        w = 5
        pygame.draw.arc(screen, BLACK, [x - side / 2 + w/2, y - side / 2 + w/2, side, side], PI + PI / 2, 0, w)
        pygame.draw.arc(screen, BLACK, [x + side + side / 2 - w/2, y + side + - side / 2 - w/2, side, side], PI / 2, PI, w)
        # if rnd == 1:
        #     pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y), (x, y + side)])
        # elif rnd == 2:
        #     pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y), (x + side, y + side)])
        # elif rnd == 3:
        #     pygame.draw.polygon(screen, BLACK, [(x + side, y), (x + side, y + side), (x, y + side)])
        # elif rnd == 4:
        #     pygame.draw.polygon(screen, BLACK, [(x, y), (x + side, y + side), (x, y + side)])
pygame.display.flip()
while True:
    pass
