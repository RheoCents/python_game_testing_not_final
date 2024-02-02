import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Platformer")

# Set up player
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height - player_height
player_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Update display
    screen.fill((255, 255, 255))  # Fill background with white
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))  # Draw player

    pygame.display.flip()
