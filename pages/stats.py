import pygame
from variables import *

def stats(playing):
    timeArrowLeft = time() - 0.1
    timeArrowRight = time() - 0.1
    timeArrowUp = time() - 0.1
    timeArrowDown = time() - 0.1
    selectedCube = 0
    selectedDate = 0
    listOfScores = []
    listOfDates = []
    overAll = False
    switched = True
    for i in range(len(listOfCubes)):
        listOfCubes[i][1].rect = listOfCubes[i][1].surface.get_rect(topright=(width -20, 0))
    while playing:
        screen.fill((255,255,255))
        if not overAll and switched:
            for score in data[listOfCubes[selectedCube][1].text]:
                date = Text(screen, score['date'].replace("-", "/"), font75, BLACK, (width - 225, height - 100))
                if listOfDates != []:
                    if listOfDates[-1].text != score['date'].replace("-", "/"):
                        listOfDates.append(date)
                else:
                    listOfDates.append(date)
                listOfScores.append([date, float(score['time'])])
            switched = False
        elif overAll and switched:
            for score in data[listOfCubes[selectedCube][1].text]:
                listOfScores.append(float(score['time']))
            switched = False
        #pos mouse
        posMouse = pygame.mouse.get_pos()
        posX = posMouse[0]
        posY = posMouse[1]
        if exitButton.checkMouse(posX, posY):
            exitButton.color = (180,255,50)
        else:
            exitButton.bgColor = BLACK
            exitButton.color = RED
        if overAllStatsButton.checkMouse(posX, posY):
            overAllStatsButton.color = (180,255,50)
        else:
            overAllStatsButton.bgColor = BLACK
            overAllStatsButton.color = RED

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
        if not overAll and len(set(listOfDates)) > 1:
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
        try:
            if not overAll:
                total = 0
                ctr = 0
                best = 9999
                worst = 0
                for score in listOfScores:
                    if score[0].text == listOfDates[selectedDate].text:
                        total+=round(score[1],2)
                        ctr+=1
                        if score[1] > worst:
                            worst = score[1]
                        if score[1] < best:
                            best = score[1]
                avg = round(total / ctr,2)
                avgText = Text(screen, "Average : {0}".format(avg), font125, BLACK, (width / 2, height / 2.5 - 150))
                bestText = Text(screen, "Best : {0}".format(best), font125, GREEN, (width / 2, height / 2.5))
                worstText = Text(screen, "Worst : {0}".format(worst), font125, RED, (width / 2, height / 2.5 + 150))
                listOfDates[selectedDate].display()
            else:
                avg = round(sum(listOfScores) / len(listOfScores),2)
                best = min(listOfScores)
                worst = max(listOfScores)
                avgText = Text(screen, "Average : {0}".format(avg), font125, BLACK, (width / 2, height / 2.5 - 150))
                bestText = Text(screen, "Best : {0}".format(best), font125, GREEN, (width / 2, height / 2.5))
                worstText = Text(screen, "Worst : {0}".format(worst), font125, RED, (width / 2, height / 2.5 + 150))
            avgText.display()
            bestText.display()
            worstText.display()
        except:
            noData = Text(screen, "No Data", font200, BLACK, (width/2, height / 2.5))
            noData.display()
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
                elif overAllStatsButton.checkMouse(posX, posY):
                    
                    if overAllStatsButton.text == "OVER ALL STATS":
                        overAllStatsButton.text = "   DAILY    STATS"
                        overAll = True
                        switched = True
                        listOfScores = []
                        listOfDates = []
                    else:
                        overAllStatsButton.text = "OVER ALL STATS"
                        overAll = False
                        switched = True
                        listOfScores = []
                        listOfDates = []
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    timeArrowLeft = time()
                    listOfDates = []
                    listOfScores = []
                    switched = True
                    if selectedCube-1 > - len(listOfCubes):
                        selectedCube -=1
                    else:
                        selectedCube = 0
                elif event.key == K_RIGHT:
                    timeArrowRight = time()
                    listOfDates = []
                    listOfScores = []
                    switched = True
                    if selectedCube+1 < len(listOfCubes):
                        selectedCube +=1
                    else:
                        selectedCube = 0
                elif event.key == K_UP:
                    timeArrowUp = time()
                    if selectedDate-1 > - len(listOfDates):
                        selectedDate -=1
                    else:
                        selectedDate = 0
                elif event.key == K_DOWN:
                    timeArrowDown = time()
                    if selectedDate +1 < len(listOfDates):
                        selectedDate += 1
                    else:
                        selectedDate = 0
        listOfCubes[selectedCube][1].display()
        overAllStatsButton.display()
        exitButton.display()
        pygame.display.flip()
    screen.fill((255,255,255))
    return True
        