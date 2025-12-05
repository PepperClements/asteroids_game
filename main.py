import pygame
from pygame import display
from constants import SCREEN_WIDTH, SCREEN_HEIGHT   
from logger import log_state

pygame.init()



def draw_screen():
    pygame.time.Clock 
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        display.flip()
        pygame.time.Clock().tick(60) 
        dt=pygame.time.Clock().tick(60) / 1000
        



draw_screen()



def main():
    print("Starting Asteroids with pygame version: ", pygame.__version__)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    


if __name__ == "__main__":
    main()
