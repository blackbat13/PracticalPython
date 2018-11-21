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
width = 900
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

draw_centers = False

radius = 40

speedX = 1
speedY = 1

ballX = width / 2
ballY = height / 2

power = 500

centers = []
centers.append({'x': 200, 'y': 400, 'power': power})
centers.append({'x': 700, 'y': 400, 'power': power})

screen.fill(WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = event.__dict__['button']
            pos = event.__dict__['pos']
            print(event)
            if button == 1:
                centers.append({'x': pos[0], 'y': pos[1], 'power': power})
            elif button == 3:
                ballX = pos[0]
                ballY = pos[1]
                speedX = random.randint(0, 2)
                speedY = random.randint(0, 2)

    pygame.draw.circle(screen, GREEN, [int(ballX + 3), int(ballY + 3)], radius)

    for center in centers:
        diffX = center['x'] - ballX
        diffY = center['y'] - ballY
        distance = math.sqrt(diffX ** 2 + diffY ** 2)
        force = center['power'] / (distance ** 2)
        forceX = force * diffX / distance
        forceY = force * diffY / distance

        speedX += forceX
        speedY += forceY

    # Apply speed to ball
    ballX += speedX
    ballY += speedY

    if ballX >= width or ballX <= 0:
        speedX *= -1
    if ballY >= height or ballY <= 0:
        speedY *= -1

    pygame.draw.circle(screen, RED, [int(ballX), int(ballY)], radius)

    if draw_centers:
        for center in centers:
            pygame.draw.circle(screen, BLACK, [int(center['x']), int(center['y'])], radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
