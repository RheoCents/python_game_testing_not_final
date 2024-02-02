import pygame
from pygame.locals import *

pygame.init()

game_screen = pygame.display.set_mode((1000,650))
pygame.display.set_caption("Rheo's world")

#images 
bg_image = pygame.image.load('Untitled design (2).png')

game_on = True
while game_on:
    game_screen.blit(bg_image, (0,0,))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    
    pygame.display.update()
pygame.quit()