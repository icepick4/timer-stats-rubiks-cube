"""MODULES"""
import pygame
from functions import getPosMouse, hover, createTriangleDown, createTriangleLeft, createTriangleRight, createTriangleUp, resetArrowLeft, resetArrowRight, toMinutes
from variables import *

def overAllButton(overAll,state):
    """changing state of overAllButton"""
    if state == "OVER ALL STATS":
        state = "   DAILY    STATS"
        overAll = True
    else:
        state = "OVER ALL STATS"
        overAll = False
    return overAll, state

def resetVar():
    """reset vars"""
    return [], [], True

def fillDicos(dico, dicoBool, data, currentCube):
    """fill the dicos of stats page"""
    if not dicoBool["overAll"] and dicoBool["switched"]:
        for score in data[currentCube.text]:
            dateText = Text(
                            screen,
                            score['date'].replace("-", "/"),
                            font75, BLACK,
                            (width - 225, height - 100)
                            )
            try:
                if dico["listOfDates"][-1].text != score['date'].replace("-", "/"):
                    dico["listOfDates"].append(dateText)
            except IndexError:
                dico["listOfDates"].append(dateText)
            dico["listOfScores"].append([dateText, float(score['time'])])
        dicoBool["switched"] = False
    elif dicoBool["overAll"] and dicoBool["switched"]:
        for score in data[currentCube.text]:
            dico["listOfScores"].append(float(score['time']))
        dicoBool["switched"] = False
    return dico

def giveStats(listOfScores, listOfDates, selectedDate, overAll):
    """returning the stats of a list of scores"""
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
    else:
        avg = round(sum(listOfScores) / len(listOfScores),2)
        best = min(listOfScores)
        worst = max(listOfScores)
    if avg > 60:
        avg = toMinutes(avg)
    if best > 60:
        best = toMinutes(best)
    if worst > 60:
        worst = toMinutes(worst)
    return avg, best, worst

def initCubesStats(listOfCubes):
    """init pos of cubes in stats page"""
    for cube in listOfCubes:
        cube[1].rect, cube[0] = cube[1].surface.get_rect(
                                                        topright=(
                                                                width -10,
                                                                10
                                                                )
                                                ), pygame.transform.smoothscale(cube[0], (150,135))
    return listOfCubes

def createArrows(overAll, date, timerArrows)
    createTriangleRight(timerArrows["timeArrowRight"])
    createTriangleLeft(timerArrows["timeArrowLeft"])
    if not overAll and date:
        createTriangleDown(timerArrows["timeArrowDown"])
        createTriangleUp(timerArrows["timeArrowUp"])

def stats(playing):
    """STATS PAGE"""
    timerArrows = {
        "timeArrowLeft":time() - 0.1,
        "timeArrowRight" : time() - 0.1,
        "timeArrowUp" : time() - 0.1,
        "timeArrowDown" : time() - 0.1
    }
    dico = {
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
        currentCube = cubes[dico["selectedCube"]][1]
        screen.fill((255,255,255))
        #display selected stats
        if dicoBool["switched"]:
            dico = fillDicos(dico, dicoBool, data, currentCube)
        #pos mouse
        posX, posY = getPosMouse()
        #####HOVER#####
        hover(posX, posY)
        #####ARROWS#####
        createArrows(dicoBool["overAll"], len(dico["listOfDates"]) > 1, timerArrows)
        try:
            avg, best, worst = giveStats(dico["listOfScores"],
                                         dico["listOfDates"],
                                         dico["selectedDate"],
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
            if not dicoBool["overAll"]:
                dico["listOfDates"][dico["selectedDate"]].display()
        except ZeroDivisionError:
            Text(screen, "No data", font200, BLACK, (width/2, height / 2.5)).display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if exitButton.checkMouse(posX, posY):
                    playing = False
                elif overAllStatsButton.checkMouse(posX, posY):
                    dicoBool["overAll"], overAllStatsButton.text = overAllButton(
                                                            overAllStatsButton.text,
                                                            overAllStatsButton.text
                                                            )
                    dico["listOfDates"],dico["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                dico["selectedCube"],timerArrows["timeArrowLeft"] = resetArrowLeft(
                                                dico["selectedCube"],
                                                len(cubes)
                                                )
                dico["listOfDates"],dico["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                dico["selectedCube"],timerArrows["timeArrowRight"] = resetArrowRight(
                                            dico["selectedCube"],
                                            len(cubes)
                                            )
                dico["listOfDates"],dico["listOfScores"],dicoBool["switched"]=resetVar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                dico["selectedDate"],timerArrows["timeArrowUp"] = resetArrowLeft(
                                            dico["selectedDate"],
                                            len(dico["listOfDates"])
                                            )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                dico["selectedDate"],timerArrows["timeArrowDown"] = resetArrowRight(
                                            dico["selectedDate"],
                                            len(dico["listOfDates"])
                                            )
        cubes[dico["selectedCube"]][1].display()
        screen.blit(cubes[dico["selectedCube"]][0], (width - 150, 75))
        overAllStatsButton.display()
        exitButton.display()
        pygame.display.flip()
    return True
        