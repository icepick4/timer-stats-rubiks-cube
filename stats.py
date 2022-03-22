"""MODULES"""
import pygame
from functions import *
from variables import *

def stats(playing):
    """STATS PAGE"""
    timerArrows = {
        "timeArrowLeft":time() - 0.1,
        "timeArrowRight" : time() - 0.1,
        "timeArrowUp" : time() - 0.1,
        "timeArrowDown" : time() - 0.1
    }
    dicoOfData = {
        "selectedCube":0,
        "selectedDate":0,
        "listOfScores": [],
        "listOfDates":[]
    }
    dicoBool = {
        "overAll" : False,
        "switched" : True
    }
    cubes = initCubesStats(listOfCubes)
    while playing:
        currentCube = cubes[dicoOfData["selectedCube"]][1]
        screen.fill((255,255,255))
        #display selected stats
        if dicoBool["switched"]:
            dicoOfData = fillDicos(dicoOfData, dicoBool, data, currentCube)
        #pos mouse
        posX, posY = getPosMouse()
        #####HOVER#####
        hover(posX, posY)

        #####ARROWS#####
        createTriangleRight(timerArrows["timeArrowRight"])
        createTriangleLeft(timerArrows["timeArrowLeft"])
        if not dicoBool["overAll"] and len(dicoOfData["listOfDates"]) > 1:
            createTriangleDown(timerArrows["timeArrowDown"])
            createTriangleUp(timerArrows["timeArrowUp"])
        try:
            avg, best, worst = giveStats(dicoOfData["listOfScores"],
                                         dicoOfData["listOfDates"],
                                         dicoOfData["selectedDate"],
                                         dicoBool["overAll"]
                                         )
            Text(
                screen,
                f"Average : {avg}",
                font125, BLACK,
                (width / 2, height / 2.5 - 150)
            ).display()
            Text(
                screen,
                f"Best : {best}",
                font125, GREEN,
                (width / 2, height / 2.5)
            ).display()
            Text(
                screen,
                f"Worst : {worst}",
                font125,
                RED,
                (width / 2, height / 2.5 + 150)
            ).display()
            if dicoBool["overAll"]:
                dicoOfData["listOfDates"][dicoOfData["selectedDate"]].display()
        except ZeroDivisionError:
            Text(screen, "No data", font200, BLACK, (width/2, height / 2.5)).display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
                elif overAllStatsButton.checkMouse(posX, posY):
                    dicoBool["overAll"], overAllStatsButton.text = overAllButton(overAllStatsButton.text,overAllStatsButton.text)
                    dicoOfData["listOfDates"],dicoOfData["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                dicoOfData["selectedCube"],timerArrows["timeArrowLeft"] = resetArrow(
                                                dicoOfData["selectedCube"],
                                                len(cubes)
                                                )
                dicoOfData["listOfDates"],dicoOfData["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                dicoOfData["selectedCube"],timerArrows["timeArrowRight"] = resetArrow(
                                            dicoOfData["selectedCube"],
                                            len(cubes)
                                            )
                dicoOfData["listOfDates"],dicoOfData["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                dicoOfData["selectedDate"],timerArrows["timeArrowUp"] = resetArrow(
                                            dicoOfData["selectedDate"],
                                            len(dicoOfData["listOfDates"])
                                            )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                dicoOfData["selectedDate"],timerArrows["timeArrowDown"] = resetArrow(
                                            dicoOfData["selectedDate"],
                                            len(dicoOfData["listOfDates"])
                                            )
        cubes[dicoOfData["selectedCube"]][1].display()
        screen.blit(cubes[dicoOfData["selectedCube"]][0], (width - 150, 75))
        overAllStatsButton.display()
        exitButton.display()
        pygame.display.flip()
    return True
        