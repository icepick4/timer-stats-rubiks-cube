from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

def mainMenu(): 
    playing = True
    while playing:
        #pos mouse
        posMouse = pygame.mouse.get_pos()
        posX = posMouse[0]
        posY = posMouse[1]

        if endButton.checkMouse(posX, posY):
            endButton.bgColor = (50,50,50)
            endButton.color = (180,255,50)
        else:
            endButton.bgColor = BLACK
            endButton.color = RED

        if statsButton.checkMouse(posX, posY):
            statsButton.bgColor = (50,50,50)
            statsButton.color = (180,255,50)
        else:
            statsButton.bgColor = BLACK
            statsButton.color = RED

        if timerButton.checkMouse(posX, posY):
            timerButton.bgColor = (50,50,50)
            timerButton.color = (180,255,50)
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
                    #stats screen
                    pass
                elif timerButton.checkMouse(posX, posY):
                    #timer screen
                    pass
        statsButton.display()
        timerButton.display()
        endButton.display()
        pygame.display.flip()
    pygame.quit()