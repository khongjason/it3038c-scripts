import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()

	
DISPLAYSURF = pygame.display.set_mode((300,300))
















while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()