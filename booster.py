import pygame
from circleshape import CircleShape
from constants import *


class booster (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.square(screen, "blue",self.position,self.radius, LINE_WIDTH)
    def update(self, dt):
         self.position += (self.velocity * dt)
    def boost(self,player):
        player.velocity += self.velocity