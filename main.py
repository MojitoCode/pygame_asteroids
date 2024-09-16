# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	
	#initialize groups to contain updatable, drawable, and asteroid items
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	#add player to the newly created groups above
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

	#initializing player, clock, and asteroid field objects
	newPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	newClock = pygame.time.Clock()
	newAsteroidField = AsteroidField()

	#initializing "Delta Time" variable
	dt = 0

	#setting game UI window
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#starting main game loop
	while True:
		for event in pygame.event.get():
			#exit loop when window X is clicked
			if event.type == pygame.QUIT:
				return
		#set window BG to black
		screen.fill((0,0,0))
		#initialize player character on screen
		for item in drawable:
			item.draw(screen)
		#initialize player movement
		for item in updatable:
			item.update(dt)
		#refresh page
		pygame.display.flip()
		dt = newClock.tick(60) / 1000

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
