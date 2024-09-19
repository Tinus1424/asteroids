from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           [255, 255, 255],
                           center = self.position, 
                           radius = self.radius, 
                           width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            angle = random.uniform(20, 50)
            a1 = self.velocity.rotate(angle)
            a2 = self.velocity.rotate(-angle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], newradius)
            asteroid2 = Asteroid(self.position[0], self.position[1], newradius)
            asteroid1.velocity = a1 * 1.2
            asteroid2.velocity = a2 * 1.2
        