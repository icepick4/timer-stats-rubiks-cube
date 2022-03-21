"""MODULES"""
from time import time
import pygame
from functions import createTriangleDown, createTriangleLeft, createTriangleRight, createTriangleUp, giveStats, getPosMouse
from variables import *


def stats(playing):
    """STATS PAGE"""
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
    for cube in listOfCubes:
        cube[1].rect = cube[1].surface.get_rect(topright=(width -10, 10))
        cube[0] = pygame.transform.smoothscale(cube[0], (150,135))
    while playing:
        currentCube = listOfCubes[selectedCube][1]
        screen.fill((255,255,255))
        #display selected stats
        if not overAll and switched:
            for score in data[currentCube.text]:
                dateText = Text(
                                screen,
                                score['date'].replace("-", "/"),
                                font75, BLACK,
                                (width - 225, height - 100)
                                )
                try:
                    if listOfDates[-1].text != score['date'].replace("-", "/"):
                        listOfDates.append(dateText)
                except IndexError:
                    listOfDates.append(dateText)
                listOfScores.append([dateText, float(score['time'])])
            switched = False
        elif overAll and switched:
            for score in data[currentCube.text]:
                listOfScores.append(float(score['time']))
            switched = False

        #pos mouse
        posX, posY = getPosMouse()

        #####HOVER#####
        if exitButton.checkMouse(posX, posY):
            exitButton.color = GREENHOVER
        else:
            exitButton.bgColor = BLACK
            exitButton.color = RED
        if overAllStatsButton.checkMouse(posX, posY):
            overAllStatsButton.color = GREENHOVER
        else:
            overAllStatsButton.bgColor = BLACK
            overAllStatsButton.color = RED

        #####ARROWS#####
        createTriangleRight(timeArrowRight)
        createTriangleLeft(timeArrowLeft)
        if not overAll and len(listOfDates) > 1:
            createTriangleDown(timeArrowDown)
            createTriangleUp(timeArrowUp)
        try:
            avg, best, worst = giveStats(listOfScores, listOfDates, selectedDate, overAll)
            avgText = Text(
                            screen,
                            f"Average : {avg}",
                            font125, BLACK,
                            (width / 2, height / 2.5 - 150)
                        )
            bestText = Text(
                            screen,
                            f"Best : {best}",
                            font125, GREEN,
                            (width / 2, height / 2.5)
                            )
            worstText = Text(
                            screen,
                            f"Worst : {worst}",
                            font125,
                            RED,
                            (width / 2, height / 2.5 + 150)
                            )
            listOfDates[selectedDate].display()
            avgText.display()
            bestText.display()
            worstText.display()
        except ZeroDivisionError:
            noData = Text(screen, "No data", font200, BLACK, (width/2, height / 2.5))
            noData.display()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    timeArrowLeft = time()
                    listOfDates = []
                    listOfScores = []
                    switched = True
                    if selectedCube-1 > - len(listOfCubes):
                        selectedCube -=1
                    else:
                        selectedCube = 0
                elif event.key == pygame.K_RIGHT:
                    timeArrowRight = time()
                    listOfDates = []
                    listOfScores = []
                    switched = True
                    if selectedCube+1 < len(listOfCubes):
                        selectedCube +=1
                    else:
                        selectedCube = 0
                elif event.key == pygame.K_UP:
                    timeArrowUp = time()
                    if selectedDate-1 > - len(listOfDates):
                        selectedDate -=1
                    else:
                        selectedDate = 0
                elif event.key == pygame.K_DOWN:
                    timeArrowDown = time()
                    if selectedDate +1 < len(listOfDates):
                        selectedDate += 1
                    else:
                        selectedDate = 0
        listOfCubes[selectedCube][1].display()
        screen.blit(listOfCubes[selectedCube][0], (width - 150, 75))
        overAllStatsButton.display()
        exitButton.display()
        pygame.display.flip()
    screen.fill((255,255,255))
    return True
        