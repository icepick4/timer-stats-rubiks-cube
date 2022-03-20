import pygame
from variables import *

def timer(playing):
    screen.fill((255,255,255))
    selectedCube = 0
    startTime = time()
    timeArrowLeft = time() - 0.2
    timeArrowRight = time() - 0.2
    inChrono = False
    holding = False
    chrono = 0.0
    while playing:
        #pos mouse
        screen.fill((255,255,255))
        posMouse = pygame.mouse.get_pos()
        posX = posMouse[0]
        posY = posMouse[1]
        if exitButton.checkMouse(posX, posY):
            exitButton.color = (180,255,50)
        else:
            exitButton.bgColor = BLACK
            exitButton.color = RED

        #statement of pushing arrow or not 
        if time() - timeArrowLeft > 0.2:
            pygame.draw.polygon(screen, BLACK, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
        if time() - timeArrowRight > 0.2:
            pygame.draw.polygon(screen, BLACK, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    timeArrowLeft = time()
                    if selectedCube-1 > - len(listOfCubes):
                        selectedCube -=1
                    else:
                        selectedCube = 0
                elif event.key == K_RIGHT:
                    timeArrowRight = time()
                    if selectedCube+1 < len(listOfCubes):
                        selectedCube +=1
                    else:
                        selectedCube = 0
                elif event.key == K_SPACE:
                    if inChrono:
                        inChrono = False
                    holding = True
                    startHolding = time()
                    
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    if time() - startHolding > 0.5:
                        inChrono = True
                        startTime = time()
                    else:
                        holding = False
        

        exitButton.display()
        timerHeader.display()
        listOfCubes[selectedCube][1].display()
        screen.blit(listOfCubes[selectedCube][0], cubesRect)

        if inChrono:    
            screen.fill((255,255,255))       
            chrono = time() - startTime
        if inChrono:
            chronoText = font300.render("{0}".format(round(chrono, 2)), True, BLACK)
        elif holding and time() - startHolding < 0.5:
            chronoText = font300.render("{0}".format(round(chrono, 2)), True, RED)  
        elif holding and time() - startHolding > 0.5:
            screen.fill((255,255,255)) 
            chronoText = font300.render("0.0", True, GREEN)  
        else:
            chronoText = font300.render("{0}".format(round(chrono, 2)), True, BLACK)

        screen.blit(chronoText, (width / 2 - 250, height / 2 - 200))

        pygame.display.flip()
    screen.fill((255,255,255))
    return True