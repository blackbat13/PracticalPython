import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

radius = 20

angle = 0

distance = 30

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    for cx in range(distance, width, distance):
        for cy in range(distance, height, distance):
            x_distance = cx/distance
            y_distance = cy/distance
            n_angle = angle + 10*x_distance + 10*y_distance
            n_angle %= 360
            x = cx + radius * math.cos(math.radians(n_angle))
            y = cy + radius * math.sin(math.radians(n_angle))
            x = int(x)
            y = int(y)

            pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)

    angle += 1
    angle %= 360

    pygame.display.flip()

    clock.tick(0)

# Close the window and quit.
pygame.quit()
