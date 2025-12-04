import pygame
from pygame import display
from constants import SCREEN_WIDTH, SCREEN_HEIGHT   
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_screen():
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        display.flip()

draw_screen()



def main():
    print("Starting Asteroids with pygame version: ", pygame.__version__)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
