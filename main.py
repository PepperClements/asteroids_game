import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
from score import display_score, update_score
from boosters import Booster


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    boosters = pygame.sprite.Group()
    Booster.containers = (updatable,drawable,boosters)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable,drawable,shots)
    Asteroid.containers = (updatable,drawable,asteroids)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = 0
    dt = 0
    

    while True:
        log_state()
        booster = Booster(400, 300, 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print(" Game Over!")
                print( f"Final Score: {score}")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    score= update_score(score,10)
                    log_event("asteroid_shot")
        screen.fill("black")
        
        for booster in boosters:
            booster.update(dt)
            booster.draw(screen)
            if player.collides_with(booster):
                booster.boost(player)
                log_event("player_boosted")
                booster.kill()

        for d in drawable:
            d.draw(screen)

        
        display_score(screen,score)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

