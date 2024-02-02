#initialization 
import pygame
from pygame.locals import *
pygame.init()

#display 
game_screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Rheo's world")

#assets
bg_image = pygame.image.load('Background.png')

#grid for working on the project (you mau delete it)
def grid_lines():
    for i in range (0, 1000, 100):
        pygame.draw.line(game_screen,(255,255,255), (i, 0), (i, 700))
        pygame.draw.line(game_screen,(255,255,255), (0, i), (1000, i))

#world building
class World_build():
    def init (self, data):
            #images
            ground_image = pygame.image.load('light_block.png')

            #loop for blocks
            row_count = 0
            for row in data:
                 collumn_count = 0
                 for tile in row:
                      if tile == 1:
                           img = pygame.transform.scale(100,100)
                           image_block = img.get_rect()
                           image_block.x = collumn_count * 100
                           image_block.y = row_count * 100
                      collumn_count += 1
                 row_count += 1

#plotting th world           
world_build = list()
world_build.append([1,1,1,1,1,1,1,1,1,1])
world_build.append([1,0,0,0,0,0,0,0,0,1]) 
world_build.append([1,0,0,0,0,0,0,0,0,1]) 
world_build.append([1,0,0,0,0,0,0,0,0,1]) 
world_build.append([1,0,0,0,0,0,0,0,0,1]) 
world_build.append([1,0,0,0,0,0,0,0,0,1]) 
world_build.append([1,1,1,1,1,1,1,1,1,1])

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