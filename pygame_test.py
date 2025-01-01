import pygame

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Window")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white
    screen.fill((255, 255, 255))
    pygame.display.flip()

# Quit Pygame
pygame.quit()