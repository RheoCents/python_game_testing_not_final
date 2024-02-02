import pygame
from pygame.locals import *

pygame.init()

game_screen = pygame.display.set_mode((1000,650))
pygame.display.set_caption("rheo's world")
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
pygame.quit()