import pygame

def display_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    

def update_score(current_score, points):
    return current_score + points