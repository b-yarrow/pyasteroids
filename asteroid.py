import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            print(random_angle)
            new_vector_one = self.velocity.rotate(random_angle)
            new_vector_two = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_one.velocity = new_vector_one * 1.2

            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two.velocity = new_vector_two * 1.2



    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

