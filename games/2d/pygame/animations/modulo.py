import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Modulo animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

count = 0

# kierunek
direction = 1
# klatka
frame = 0

square_size = 17

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

    square_width = int(width / square_size)
    square_height = int(height / square_size)

    for i in range(1, square_size + 1):
        for j in range(1, square_size + 1):
            x = square_width * (i - 1)
            y = square_height * (j - 1)
            value = (i * j) % square_size
            cl = int(value * (255 / square_size))

            color = (255 - cl, 0, cl)
            pygame.draw.rect(screen, color, (x, y, square_width, square_height))

    square_size += 1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(1)

# Close the window and quit.
pygame.quit()
