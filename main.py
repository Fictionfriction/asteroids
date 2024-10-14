import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    asteroidz = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        for object in drawable:
            object.draw(screen)

        for object in updatable:
            object.update(dt)

        pygame.display.update()

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()