import pygame
from variables import *

def stats(playing):
    timeArrowLeft = time() - 0.1
    timeArrowRight = time() - 0.1
    timeArrowUp = time() - 0.1
    timeArrowDown = time() - 0.1
    selectedCube = 0
    selectedDate = 0
    listOfDates = []
    listOfTimes = []
    for i in range(len(listOfCubes)):
        listOfCubes[i][1].rect = listOfCubes[i][1].surface.get_rect(topright=(width -20, 0))
    while playing:
        screen.fill((255,255,255))
        for score in data[listOfCubes[selectedCube][1].text]:
            listOfDates.append(Text(screen, score['date'].replace("-", "/"), font75, BLACK, (width - 225, height - 100)))
            listOfTimes.append(float(score['time']))
        #pos mouse
        posMouse = pygame.mouse.get_pos()
        posX = posMouse[0]
        posY = posMouse[1]

        if exitButton.checkMouse(posX, posY):
            exitButton.color = (180,255,50)
        else:
            exitButton.bgColor = BLACK
            exitButton.color = RED

        #left
        if time() - timeArrowLeft > 0.1:
            pygame.draw.polygon(screen, BLACK, [(20, height / 2), (100, height / 2.2), (100, height / 1.8)])
        else:
            pygame.draw.polygon(screen, RED, [(20, height / 2), (100, height / 2.2), (100, height / 1.8)])
        #right
        if time() - timeArrowRight > 0.1:
            pygame.draw.polygon(screen, BLACK, [(width - 20, height / 2), (width - 100, height / 2.2), (width - 100, height / 1.8)])
        else:
            pygame.draw.polygon(screen, RED, [(width - 20, height / 2), (width - 100, height / 2.2), (width - 100, height / 1.8)])
        #up
        if time() - timeArrowUp > 0.1:
            pygame.draw.polygon(screen, BLACK, [(width / 2, 20), (width / 2 + width * 0.03, 100), (width / 2 - width * 0.03, 100)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2, 20), (width / 2 + width * 0.03, 100), (width / 2 - width * 0.03, 100)])
        #down
        if time() - timeArrowDown > 0.1:
            pygame.draw.polygon(screen, BLACK, [(width / 2, height - 20), (width / 2 + width * 0.03, height - 100), (width / 2 - width * 0.03, height - 100)])
        else:
            pygame.draw.polygon(screen, RED, [(width / 2, height - 20), (width / 2 + width * 0.03, height - 100), (width / 2 - width * 0.03, height - 100)])
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    timeArrowLeft = time()
                    listOfDates = []
                    listOfTimes = []
                    if selectedCube-1 > - len(listOfCubes):
                        selectedCube -=1
                    else:
                        selectedCube = 0
                elif event.key == K_RIGHT:
                    timeArrowRight = time()
                    listOfDates = []
                    listOfTimes = []
                    if selectedCube+1 < len(listOfCubes):
                        selectedCube +=1
                    else:
                        selectedCube = 0
                if event.key == K_UP:
                    timeArrowUp = time()
                    if selectedDate-1 > - len(listOfDates):
                        selectedDate -=1
                    else:
                        selectedDate = 0
                elif event.key == K_DOWN:
                    timeArrowDown = time()
                    if selectedDate+1 < len(listOfDates):
                        selectedDate +=1
                    else:
                        selectedCube = 0
        try:
            avg = round(sum(listOfTimes) / len(listOfTimes),2)
            best = min(listOfTimes)
            worst = max(listOfTimes)
            avgText = Text(screen, "Average : {0}".format(avg), font125, BLACK, (width / 2, height / 2.5 - 150))
            bestText = Text(screen, "Best : {0}".format(best), font125, GREEN, (width / 2, height / 2.5))
            worstText = Text(screen, "Worst : {0}".format(worst), font125, RED, (width / 2, height / 2.5 + 150))
            avgText.display()
            bestText.display()
            worstText.display()
            listOfDates[selectedDate].display()
        except:
            noData = Text(screen, "No Data", font200, BLACK, (width/2, height / 2.5))
            noData.display()
        listOfCubes[selectedCube][1].display()
        
        exitButton.display()
        pygame.display.flip()
    screen.fill((255,255,255))
    return True
        