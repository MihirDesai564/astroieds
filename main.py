# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys 
from constant import *
from player import Player
from asteroidsfield import AsteroidField
from asteroids import Asteroid
from shots import Shot

def main():
    print("starting astroieds")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 

    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable
    asteroids_field = AsteroidField()

    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.CollisionChecker(player):
                print("Game Over")
                sys.exit()
            
            for shot in shots:
                if asteroid.CollisionChecker(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        time = clock.tick(60)
        dt = time/1000




if __name__ == "__main__":
    main()
