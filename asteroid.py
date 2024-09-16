import pygame
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.x = x
		self.y = y
		self.radius = radius
		self.velocity = pygame.Vector2(0,0)

	def draw(self, surface):
		pygame.draw.circle(surface, "white", (self.x, self.y), self.radius, 2)

	def update(self, dt_value):
		movement = self.velocity * dt_value
		self.x += movement.x
		self.y += movement.y

