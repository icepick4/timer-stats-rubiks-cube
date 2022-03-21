from variables import *
from functions import getPosMouse
from .stats import stats
from .timer import timer

try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

def mainMenu(): 
    playing = True
    while playing:
        #pos mouse
        posX, posY = getPosMouse()

        if endButton.checkMouse(posX, posY):
            endButton.color = GREENHOVER
        else:
            endButton.bgColor = BLACK
            endButton.color = RED

        if statsButton.checkMouse(posX, posY):
            statsButton.color = GREENHOVER
        else:
            statsButton.bgColor = BLACK
            statsButton.color = RED

        if timerButton.checkMouse(posX, posY):
            timerButton.color = GREENHOVER
        else:
            timerButton.bgColor = BLACK
            timerButton.color = RED

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