import pygame
from variables import *

def timer(playing):
    screen.fill((255,255,255))
    selectedCube = 0
    while playing:
        #pos mouse
        posMouse = pygame.mouse.get_pos()
        posX = posMouse[0]
        posY = posMouse[1]

        if exitButton.checkMouse(posX, posY):
            exitButton.color = (180,255,50)
        else:
            exitButton.bgColor = BLACK
            exitButton.color = RED

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pygame.draw.polygon(screen, RED, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
                    if selectedCube-1 > - len(listOfCubes):
                        selectedCube -=1
                    else:
                        selectedCube = 0
                elif event.key == K_RIGHT:
                    pygame.draw.polygon(screen, RED, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])
                    if selectedCube+1 < len(listOfCubes):
                        selectedCube +=1
                    else:
                        selectedCube = 0
                elif event.type == K_SPACE:
                    pass
            else:
                pygame.draw.polygon(screen, BLACK, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
                pygame.draw.polygon(screen, BLACK, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])

        exitButton.display()
        timerHeader.display()
        chooseTitle.display()
        pygame.draw.rect(screen, WHITE, cubesRect)
        screen.blit(listOfCubes[selectedCube], cubesRect)

        pygame.display.flip()
    screen.fill((255,255,255))
    return True