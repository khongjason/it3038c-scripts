#  LAB 7

Where taking the Pygame, an Python plugin for my Lab 7 example.  for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. 

*  First things to install

1. pip install pygame: [pip install pygame](https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/)
2. Once it downloads, in order for pygame  to function you have input these:

import pygame, sys
from pygame.locals import *
 
# Initialize program
1. pygame.init()
2. 
3. 
4. while True:
5.     pygame.display.update()
6.     for event in pygame.event.get():
7.         if event.type == QUIT:
8.             pygame.quit()
9.             sys.exit()

## Display box
1. to display a box for your program. For every game, we create a window of a fixed size by passing a tuple containing the width and height. This tuple is then passe into the display.set_mode() function.

2. DISPLAYSURF = pygame.display.set_mode((300,300))

## COLORS
1. this add color, and there are many types 

2. color1 = pygame.Color(0, 0, 0)         # Black
3. color2 = pygame.Color(255, 255, 255)   # White
4. color3 = pygame.Color(128, 128, 128)   # Grey
5. color4 = pygame.Color(255, 0, 0)       # Red
### Pygame drawing function
1. pygame.draw.line(surface, color, start_point, end_point, width)
2. pygame.draw.lines(surface, color, closed, pointlist, width)
3. pygame.draw.circle(surface, color, center_point, radius, width)

* surface parameter is the surface object on which pygame will draw the shape.
* color parameter is the designated color of the assigned shape.
* The pointlist  is a tuple containing co-ordinates or “points”. 
* width t determines the size of the outline of the shape.
* start_point and end_point represent a set of co-ordinates. 

#### OUTPUT OF THE PROJECT
1.  import pygame, sys
2. from pygame.locals import *
 
# Initialize program
3. pygame.init()
# Assign FPS a value
 4. FPS = 30
 5. FramePerSec = pygame.time.Clock()
 6. BLUE  = (0, 0, 255)
 7.  RED   = (255, 0, 0)
8. GREEN = (0, 255, 0)
9. BLACK = (0, 0, 0)
10. WHITE = (255, 255, 255)
11. DISPLAYSURF = pygame.display.set_mode((300,300))
12. DISPLAYSURF.fill(WHITE)
13. pygame.display.set_caption("Example")
14. pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
15. pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
16. pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
17. pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
18. pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
19. pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
20. pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
21. while True:
22.   pygame.display.update()
23.   for event in pygame.event.get():
24.         if event.type == QUIT:
25.            pygame.quit()
26.            sys.exit()
   

* pretty much creates the shapes, colors and displays, not processed as a game yet.