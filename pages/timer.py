import pygame
from variables import *
from functions import toMinutes
import json

def timer(playing):
    screen.fill((255,255,255))
    selectedCube = 0
    startTime = time()
    timeArrowLeft = time() - 0.1
    timeArrowRight = time() - 0.1
    inChrono = False
    holding = False
    chrono = "0.0"
    lastChronos = [0.0]
    chronoText = font200.render("{0}".format(0.00), True, BLACK)
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
        if removeButton.checkMouse(posX, posY):
            removeButton.color = (180,255,50)
        else:
            removeButton.bgColor = BLACK
            removeButton.color = RED

        #statement of pushing arrow or not 
        if time() - timeArrowLeft > 0.1:
            pygame.draw.polygon(screen, BLACK, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2 - 300, height / 1.2), (width / 2 - 200, height / 1.3), (width / 2 - 200, height / 1.1)])
        if time() - timeArrowRight > 0.1:
            pygame.draw.polygon(screen, BLACK, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2 + 300, height / 1.2), (width / 2 + 200, height / 1.3), (width / 2 + 200, height / 1.1)])

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
                if removeButton.checkMouse(posX, posY):
                    if len(lastChronos) > 1:
                        lastChronos.pop()
                    try:
                        data[listOfCubes[selectedCube][1].text].pop()
                    except:
                        #empty list
                        pass
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
                        data[listOfCubes[selectedCube][1].text].append({"time": chrono, "date":date})
                        lastChronos.append(float(chrono))
                    startHolding = time()
                    holding = True
                    
                    
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    if time() - startHolding > 0.5:
                        inChrono = True
                        startTime = time()
                    else:
                        holding = False
        lastChrono = lastChronos[-1]
        if inChrono:
            chrono = str(round(time() - startTime, 2))
        else:
            chrono = str(float(lastChrono))
        if lastChrono != 0:
            if lastChrono > 60:
                lastChrono = toMinutes(lastChrono)
            last = font75.render("Last : {0}".format(lastChrono), True, BLACK)
            screen.blit(last, (width - last.get_width() - 20, 10))
        if len(lastChronos) > 5:
            avg5 = round(sum(lastChronos[len(lastChronos) - 5: len(lastChronos)])/ 5, 2)
            if avg5 > 60:
                avg5 = toMinutes(avg5)
            ao5 = font75.render("ao5 : {0}".format(avg5), True, BLACK)
            screen.blit(ao5, (width / 1.3, 100))
        if len(lastChronos) > 12:
            avg12 = round(sum(lastChronos[len(lastChronos) - 12: len(lastChronos)])/ 12, 2)
            if avg12 > 60:
                avg12 = toMinutes(avg12)
            ao12 = font75.render("ao12 : {0}".format(avg12), True, BLACK)
            screen.blit(ao12, (width / 1.3, 200))
        exitButton.display()
        listOfCubes[selectedCube][1].display()
        screen.blit(listOfCubes[selectedCube][0], cubesRect)
        removeButton.display()
        
        if inChrono:    
            screen.fill((255,255,255))
            if float(chrono) > 60:
                chronoMinutes = toMinutes(chrono)       
                chronoText = font300.render("{0}".format(chronoMinutes), True, BLACK)
            else:
                chronoText = font300.render("{0}".format(chrono), True, BLACK)  
        elif holding and time() - startHolding < 0.5:
            chronoText = font300.render("{0}".format(chrono), True, RED)  
        elif holding and time() - startHolding > 0.5:
            screen.fill((255,255,255)) 
            chronoText = font300.render("0.0", True, GREEN)  
        else:
            if float(chrono) > 60:
                chronoMinutes = toMinutes(chrono)
                chronoText = font300.render("{0}".format(chronoMinutes), True, BLACK)
            else:
                chronoText = font300.render("{0}".format(chrono), True, BLACK)  
        screen.blit(chronoText, chronoRect)
        pygame.display.flip()
    screen.fill((255,255,255))
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return True