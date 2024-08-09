import pygame
import sys
import math

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
G = 1  # Gravitational constant

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Orbit Simulation")
clock = pygame.time.Clock()

class CelestialBody(pygame.sprite.Sprite):
    def __init__(self, color, radius, semimajor_axis, eccentricity):
        super().__init__()
        self.color = color
        self.radius = radius
        self.semimajor_axis = semimajor_axis
        self.eccentricity = eccentricity
        self.angle = 0  # Initial angle in radians
        self.update_position()

    def update_position(self):
        # Elliptical orbit equations
        self.x = WIDTH // 2 + self.semimajor_axis * math.cos(self.angle)
        self.y = HEIGHT // 2 + (self.semimajor_axis * (1 - self.eccentricity**2)) * math.sin(self.angle)

        # Update the angle for the next frame
        self.angle += 0.01  # Adjust the angular velocity as needed

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a celestial body
planet = CelestialBody(RED, 10, 100, 0.6)

all_sprites = pygame.sprite.Group()
all_sprites.add(planet)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions of celestial bodies
    all_sprites.update()

    # Drawing
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
