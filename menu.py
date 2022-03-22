from functions import getPosMouse
from variables import *
from stats import *
from timer import *

try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

def mainMenu(): 
    playing = True
    while playing:
        screen.fill((255,255,255))
        #pos mouse
        posX, posY = getPosMouse()
        hover(posX, posY)

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if endButton.checkMouse(posX, posY):
                    playing = False
                elif statsButton.checkMouse(posX, posY):
                    playing = stats(True)
                elif timerButton.checkMouse(posX, posY):
                    playing = timer(True)
        statsButton.display()
        timerButton.display()
        endButton.display()
        screen.blit(menuImage, (width / 2 - 300 / 2, 100))
        pygame.display.flip()
    pygame.quit()