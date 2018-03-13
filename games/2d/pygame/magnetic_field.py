import pygame
import random
import math


def prepare_particles(max_x, max_y):
    particles_list = []
    for i in range(0, 30):
        particle = {}
        particle['x'] = random.randint(0, max_x)
        particle['y'] = random.randint(0, max_y)
        particle['mass'] = 1
        particle['charge'] = 10
        particle['speed_x'] = 0
        particle['speed_y'] = 0
        particle['force_x'] = 0
        particle['force_y'] = 0
        particle['radius'] = 15
        particles_list.append(particle)
    return particles_list


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Magnetic Field")

done = False

clock = pygame.time.Clock()

particles_list = prepare_particles(width, height)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # Reset Forces

    for particle in particles_list:
        particle['force_x'] = 0
        particle['force_y'] = 0

    # Update Forces

    for i in range(0, len(particles_list)):
        for j in range(i + 1, len(particles_list)):
            particle1 = particles_list[i]
            particle2 = particles_list[j]
            diff_x = particle2['x'] - particle1['x']
            diff_y = particle2['y'] - particle1['y']
            distance = math.sqrt(diff_x ** 2 + diff_y ** 2)
            if distance == 0:
                continue

            force = -1 * particle1['charge'] * particle2['charge'] / (distance * distance)
            if force > 1000:
                force = 1000

            force_x = force * diff_x / distance
            force_y = force * diff_y / distance

            particle1['force_x'] += force_x
            particle1['force_y'] += force_y
            particle2['force_x'] -= force_x
            particle2['force_y'] -= force_y

    # Update Particles

    for particle in particles_list:
        particle['speed_x'] += particle['force_x'] / particle['mass']
        particle['speed_y'] += particle['force_y'] / particle['mass']
        particle['x'] += particle['speed_x']
        particle['y'] += particle['speed_y']

    # Contain Particles

    for particle in particles_list:
        if particle['x'] < 0:
            particle['x'] = 1
            particle['speed_x'] = math.fabs(particle['speed_x'])
        if particle['y'] < 0:
            particle['y'] = 1
            particle['speed_y'] = math.fabs(particle['speed_y'])
        if particle['x'] > width:
            particle['x'] = width - 1
            particle['speed_x'] = math.fabs(particle['speed_x']) * -1
        if particle['y'] > height:
            particle['y'] = height - 1
            particle['speed_y'] = math.fabs(particle['speed_y']) * -1

    # Draw Particles

    for particle in particles_list:
        pygame.draw.circle(screen, RED, [int(particle['x']), int(particle['y'])], particle['radius'])

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
