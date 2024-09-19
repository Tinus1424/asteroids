import pygame
from circleshape import *

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           [255, 255, 255],
                           center = self.position,
                           radius = self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt