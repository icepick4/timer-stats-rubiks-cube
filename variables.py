"""IMPORTING CLASSES"""
from datetime import datetime
from time import time
import glob
import json
import pygame

from classes.button import Button
from classes.text import Text

RED = (255,50,50)
YELLOW = (255,215,0)
BLACK = (0,0,0)
GREY = (50,50,50)
WHITE = (255,255,255)
GREEN = (50,255,50)
GREENHOVER = (28, 184, 48)

pygame.init()
#setting window
windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

date = datetime.today().strftime('%d-%m-%Y')

PLAYING = True

#####FONTS#####
FONTPATH = "assets/font/aAkhirTahun.ttf"
font50 = pygame.font.Font(FONTPATH, 50)
font75 = pygame.font.Font(FONTPATH, 75)
font100 = pygame.font.Font(FONTPATH, 100)
font125 = pygame.font.Font(FONTPATH, 125)
font200 = pygame.font.Font(FONTPATH, 200)
font300 = pygame.font.Font(FONTPATH, 300)
fontWidth = pygame.font.Font(FONTPATH, int(width * 0.025))
#####MENU PAGE#####
#bouton pour fermer la fenetre
endButton = Button("CLOSE", font50, RED,(width - width / 8, 20))
statsButton = Button("STATS", font125, RED,(width / 2 - 400, height / 2 +100))
timerButton = Button("TIMER", font125, RED, (width/2 +150, height / 2 +100))
exitButton = Button("EXIT", font50, RED, (20,20))
menuImage = pygame.transform.smoothscale(
    pygame.image.load("assets/image/rubik's_cube.png").convert_alpha(), (380,400)
)

with open("data.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

#####TIMER PAGE#####
timerHeader = Text(screen, "SCRAMBLE : ", font75, BLACK, (width / 10 , 20))
listOfCubesPaths = glob.glob("assets/image/cubes/*")
listOfCubes = []
for path in listOfCubesPaths:
    listOfCubes.append([
                        pygame.transform.smoothscale(
                        pygame.image.load(path).convert_alpha(), (330,300))
                        ,
                        Text(
                            screen,
                            path[19:len(path)-4].replace("_"," "),
                            font75,
                            BLACK,
                            (width / 2, height /1.7)
                            )
                        ])
cubesRect = pygame.Rect((width / 2 - 330 / 2, height / 1.5, 330,300))
chronoText = font200.render(f"{0.00}", True, BLACK)
chronoRect = chronoText.get_rect(
                                midtop=(width/2 - chronoText.get_width() / 4,
                                        height / 2 - chronoText.get_height()
                                        )
                                )
removeButton = Button(
                     "REMOVE LAST TIME",
                     fontWidth,
                     RED,
                     (width - width / 3.5, height - 100)
                     )
LASTCHRONO = 0

#####STATS PAGE#####
overAllStatsButton = Button(
                            "OVER ALL STATS",
                            font50,
                            RED,
                            (width / 30, height - height / 10)
                            )

screen.fill((255,255,255))
