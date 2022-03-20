from classes.button import Button
from classes.text import Text
from classes.font import Font
from datetime import datetime
from time import time
import glob
import pygame 
from pygame.locals import *  
pygame.init()

RED = (255,50,50)
YELLOW = (255,215,0)
BLACK = (0,0,0)
GREY = (50,50,50)
WHITE = (255,255,255)

date = datetime.today().strftime('%Y-%m-%d')

#setting window
windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

playing = True

#####FONTS#####
fontPath = "assets/font/Sweet_Pancakes.otf"
font50 = pygame.font.Font(fontPath, 50)
font75 = pygame.font.Font(fontPath, 75)
font100 = pygame.font.Font(fontPath, 100)
font125 = pygame.font.Font(fontPath, 125)

#####MENU PAGE#####
#bouton pour fermer la fenetre
endButton = Button(screen, "CLOSE", font50, BLACK, RED,(width / 1.1, 20))
statsButton = Button(screen,"STATS", font75, BLACK, RED,(width / 2 - 250, height / 2 - 50))
timerButton = Button(screen, "TIMER", font75, BLACK, RED, (width/2 +75, height / 2 - 50))
exitButton = Button(screen, "EXIT", font50, BLACK, RED, (20,20))
menuImage = pygame.transform.smoothscale(pygame.image.load("assets/image/rubik's_cube.png").convert_alpha(), (240,250))

#####TIMER PAGE#####
timerHeader = Text(screen, "TIMER", font75, BLACK, (width / 2 , 20))
chooseTitle = Text(screen, "CHOOSE YOUR CUBE", font50, BLACK, (width / 2, height /1.5))
listOfCubesPaths = glob.glob("assets/image/cubes/*")
listOfCubes = []
for path in listOfCubesPaths:
    listOfCubes.append(pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (330,300)))
cubesRect = pygame.Rect((width / 2 - 330 / 2, height / 1.4, 330,300))
timer = time() - time()
chrono = Text(screen, "{}".format(timer), font125, BLACK, (width / 2, height / 2))

statsHeader = Text(screen, "STATS", font75, BLACK, (width / 2, 20))

screen.fill((255,255,255))