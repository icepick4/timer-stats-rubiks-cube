from classes.button import Button
from classes.text import Text
from datetime import datetime
import pygame 
from pygame.locals import *  
pygame.init()

RED = (255,50,50)
YELLOW = (255,215,0)
BLACK = (0,0,0)
GREY = (50,50,50)

date = datetime.today().strftime('%Y-%m-%d')

windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

playing = True

fontPath = "assets/font/Sweet_Pancakes.otf"
font = pygame.font.Font(fontPath, 50)

#bouton pour fermer la fenetre
endButton = Button(screen, "CLOSE", font, BLACK, RED,(width / 1.1, 20))

statsButton = Button(screen,"STATS", font, BLACK, RED,(width / 2 - 200, height / 2 - 50))
timerButton = Button(screen, "TIMER", font, BLACK, RED, (width/2 +50, height / 2 - 50))
exitButton = Button(screen, "EXIT", font, BLACK, RED, (20,20))

menuImage = pygame.transform.smoothscale(pygame.image.load("assets/image/rubik's_cube.png").convert_alpha(), (240,250))

statsHeader = Text(screen, "STATS", font, BLACK, (width / 2, 20))
timerHeader = Text(screen, "TIMER", font, BLACK, (width / 2, 20))
screen.fill((255,255,255))