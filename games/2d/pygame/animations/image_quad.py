import pygame
import random
from PIL import Image
import math
import queue as Q


def count_average_and_difference(image, rectangle):
    average_color = [0, 0, 0]
    pixels_no = 0

    for x in range(rectangle[0], rectangle[0] + rectangle[2]):
        for y in range(rectangle[1], rectangle[1] + rectangle[3]):
            pixels_no += 1
            color = image.getpixel((x, y))
            average_color[0] += color[0]
            average_color[1] += color[1]
            average_color[2] += color[2]

    average_color[0] /= pixels_no
    average_color[1] /= pixels_no
    average_color[2] /= pixels_no

    average_color = (int(average_color[0]), int(average_color[1]), int(average_color[2]))

    difference = 0
    for x in range(rectangle[0], rectangle[0] + rectangle[2]):
        for y in range(rectangle[1], rectangle[1] + rectangle[3]):
            color = image.getpixel((x, y))
            difference += math.fabs(average_color[0] - color[0])
            difference += math.fabs(average_color[1] - color[1])
            difference += math.fabs(average_color[2] - color[2])

    #difference /= pixels_no
    return average_color, difference


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
image = Image.open("cat.jpg")
width, height = image.size
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Image animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

count = 0

# kierunek
direction = 1
# klatka
frame = 0

squares = Q.PriorityQueue()
rectangle = (0, 0, width, height)
average_color, difference = count_average_and_difference(image, rectangle)
squares.put((-difference, average_color, rectangle))

screen.fill(WHITE)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    square = squares.get()

    if square[2][2] <= 1 or square[2][3] <= 1:
        continue

    x = square[2][0]
    y = square[2][1]
    width_half = math.ceil(square[2][2] / 2)
    height_half = math.ceil(square[2][3] / 2)
    width_half_f = math.floor(square[2][2] / 2)
    height_half_f = math.floor(square[2][3] / 2)

    rectangle = (x, y, width_half, height_half)
    average_color, difference = count_average_and_difference(image, rectangle)
    squares.put((-difference, average_color, rectangle))
    pygame.draw.rect(screen, average_color, rectangle)

    rectangle = (x + width_half, y, width_half_f, height_half)
    average_color, difference = count_average_and_difference(image, rectangle)
    squares.put((-difference, average_color, rectangle))
    pygame.draw.rect(screen, average_color, rectangle)

    rectangle = (x, y + height_half, width_half, height_half_f)
    average_color, difference = count_average_and_difference(image, rectangle)
    squares.put((-difference, average_color, rectangle))
    pygame.draw.rect(screen, average_color, rectangle)

    rectangle = (x + width_half, y + height_half, width_half_f, height_half_f)
    average_color, difference = count_average_and_difference(image, rectangle)
    squares.put((-difference, average_color, rectangle))
    pygame.draw.rect(screen, average_color, rectangle)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
