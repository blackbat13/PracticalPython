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

cx = width / 2
cy = height / 2

radius = 200

angle = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    x = cx + radius * math.cos(math.radians(angle))
    y = cy + radius * math.sin(math.radians(angle))
    x = int(x)
    y = int(y)

    pygame.draw.circle(screen, (angle % 256, (360 - angle) % 256, (angle * 2) % 256), (x, y), 30)

    angle += 1
    angle %= 360

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
