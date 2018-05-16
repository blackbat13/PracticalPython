import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hypnotic Circles")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

count = 0

radiusChange = 0
difference = 20

screen.fill(WHITE)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Here, we clear the screen to white.
    screen.fill(BLACK)

    centerX = int(width / 2)
    centerY = int(height / 2)

    radius = int(math.sqrt((width / 2) ** 2 + (height / 2) ** 2)) + radiusChange
    radiusChange += 1
    radiusChange %= 2 * difference
    i = 0

    while radius > 0:
        color = WHITE
        if i % 2:
            color = BLACK
        pygame.draw.circle(screen, color, [centerX, centerY], radius)
        radius -= difference
        i += 1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
