# it3038c-scripts project 2

import pygame # it is a library, used to create video games; plays sound drawing graphics etc.
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 800,800    # these just the height property of image, number of channels represents/ per pixel
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()    #initializes all imported pygame modules

screen = pygame.display.set_mode((WIDTH, HEIGHT))   #function screen and rest, will se the mode of the display and return the surface object
pygame.display.set_caption("Digital Clock")   # If the display has a window title, this function will change the name on the window
clock = pygame.time.Clock()   #  to create a clock object which can be used to keep track of time
FPS = 60 # frames per second

WHITE = (255, 255, 255) # bottom three here are color code in python 
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False) # create a Font object from the system fonts function.
    text = font.render(number, True, WHITE)  #A Font object is used to create a Surface object from a string.
    text_rect = text.get_rect(center=(position)) # centers it
    screen.blit(text, text_rect)   # t's going to copy the contents of one Surface onto another Surface
     
def sin_to_cosine(r, theta): # formula used for radius
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)

def main():  # acts as the point of execution for any program
    run = True  # boolean value as false is the same as 0
    while run:  # iterate over a block of code as the test expression
    
        for event in pygame.event.get(): # Every element in this queue is an Event object and they'll all have the attribute type ,
            if event.type == pygame.QUIT:  #opposite of the pygame. init() function: it runs code that deactivates the Pygame library. 
                 run = False
        current_time = datetime.datetime.now() #imported by datetime, gets current time
        second = current_time.second # Current time to second
        minute = current_time.minute # current time to minutes
        hour =current_time.hour    # current time to hours
        
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, center, clock_radius - 10, 10)
        pygame.draw.circle(screen, WHITE, center, 12)

        for number in range(1, 13):
             numbers(str(number), 80, sin_to_cosine(clock_radius - 80, number * 30))

        for number in range(0, 360, 6): # every 6 degree is a minute
            if number % 5:
               pygame.draw.line(screen, WHITE, sin_to_cosine(clock_radius - 15, number),sin_to_cosine(clock_radius - 30, number), 2)

            else:
               pygame.draw.line(screen, WHITE, sin_to_cosine(clock_radius - 15, number), sin_to_cosine(clock_radius - 35, number), 6)
 

        r = 250 # the hour hand
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, RED, center, sin_to_cosine(r, theta), 14)  # draws the hour hand

        r = 280 # minute hand
        theta = (minute + second /60 ) * (360 / 60)
        pygame.draw.line(screen, WHITE, center, sin_to_cosine(r, theta), 10)  # draws the minute hand

        
        r = 340    #second hand
        theta = second * (360 /60)
        pygame.draw.line(screen, RED, center, sin_to_cosine(r, theta), 4) # draws the second hand ( display)

        pygame.display.update() #updates the entire Surface
         
        clock.tick(FPS) #the function will delay to keep the game running slower than the given ticks per second.
    pygame.quit() # runs code that deactivates the Pygame library.
     

main()
