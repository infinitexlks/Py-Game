import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Game')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate at 60 FPS
    clock.tick(60)
