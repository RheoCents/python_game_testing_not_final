#initialization 
import pygame
from pygame.locals import *
pygame.init()

#display 
game_screen = pygame.display.set_mode((1000,650))
pygame.display.set_caption("Rheo's world")

#assets
bg_image = pygame.image.load('Background.png')

#grid for working on the project (you mau delete it)
def grid_lines():
    for i in range (0, 1000, 50):
        pygame.draw.line(game_screen,(255,255,255), (i, 0), (i, 645))
        pygame.draw.line(game_screen,(255,255,255), (0, i), (995, i))


#game startup loop
game_on = True
while game_on:
    #backgrounds and assets
    game_screen.blit(bg_image, (0,0,))
    grid_lines()
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    
    pygame.display.update()
pygame.quit()