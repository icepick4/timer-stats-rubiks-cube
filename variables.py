from classes.button import Button
import pygame   
pygame.init()

RED = (255,50,50)
YELLOW = (255,215,0)
BLACK = (0,0,0)
GREY = (50,50,50)

windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

playing = True

fontPath = "assets/font/Sweet_Pancakes.otf"
font = pygame.font.Font(fontPath, 50)

#bouton pour fermer la fenetre
endButton = Button(screen, "CLOSE", font, BLACK, RED,(width / 1.1, 20))
statsButton = Button(screen,"STATS", font, BLACK, RED,(50,50))
timerButton = Button(screen, "TIMER", font, BLACK, RED, (width/2, height / 2))

screen.fill((255,255,255))