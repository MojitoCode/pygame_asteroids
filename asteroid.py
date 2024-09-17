import pygame
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.velocity = pygame.Vector2(0,0)

	def draw(self, surface):
		pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)

	def update(self, dt_value):
		movement = self.velocity * dt_value
		self.position += movement
