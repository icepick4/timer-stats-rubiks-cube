"""functions"""
from time import time
import pygame
from variables import screen, height, width, BLACK, RED, font75, Text, exitButton, overAllStatsButton, GREENHOVER, endButton, statsButton, timerButton

def toMinutes(chrono):
    """convert seconds to minute display"""
    return "{0}:{1}".format(int(float(chrono)/60), round(float(chrono) - (float(chrono) // 60) * 60, 2))

def createTriangleLeft(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                                screen,
                                BLACK, 
                                [(20, height / 2),
                                (100, height / 2.2),
                                (100, height / 1.8)]
                                )
    else:
        pygame.draw.polygon(
                                screen,
                                RED, 
                                [(20, height / 2),
                                (100, height / 2.2),
                                (100, height / 1.8)]
                                )

def createTriangleRight(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                            screen,
                            BLACK,
                            [(width - 20, height / 2),
                            (width - 100, height / 2.2),
                            (width - 100, height / 1.8)]
                            )
    else:
        pygame.draw.polygon(
                            screen,
                            RED,
                            [(width - 20, height / 2),
                            (width - 100, height / 2.2),
                            (width - 100, height / 1.8)]
                            )

def createTriangleUp(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                                screen,
                                BLACK,
                                [(width / 2, 20),
                                (width / 2 + width * 0.03, 100),
                                (width / 2 - width * 0.03, 100)]
                                )
    else:
        pygame.draw.polygon(
                                screen,
                                RED,
                                [(width / 2, 20),
                                (width / 2 + width * 0.03, 100),
                                (width / 2 - width * 0.03, 100)]
                                )

def createTriangleDown(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                            screen,
                            BLACK,
                            [(width / 2, height - 20),
                            (width / 2 + width * 0.03,height - 100),
                            (width / 2 - width * 0.03, height - 100)]
                            )
    else:
        pygame.draw.polygon(
                            screen,
                            RED,
                            [(width / 2, height - 20),
                            (width / 2 + width * 0.03,height - 100),
                            (width / 2 - width * 0.03, height - 100)]
                            )

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

def getPosMouse():
    posMouse = pygame.mouse.get_pos()
    return (posMouse[0], posMouse[1])

def fillDicos(dicoOfData, dicoBool, data, currentCube):
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
                if dicoOfData["listOfDates"][-1].text != score['date'].replace("-", "/"):
                    dicoOfData["listOfDates"].append(dateText)
            except IndexError:
                dicoOfData["listOfDates"].append(dateText)
            dicoOfData["listOfScores"].append([dateText, float(score['time'])])
        dicoBool["switched"] = False
    elif dicoBool["overAll"] and dicoBool["switched"]:
        for score in data[currentCube.text]:
            dicoOfData["listOfScores"].append(float(score['time']))
        dicoBool["switched"] = False
    return dicoOfData

def resetArrow(selection, length):
    """reset an arrow"""
    if selection-1 > - length:
        selection -=1
    else:
        selection = 0
    return selection, time()

def resetVar():
    """reset vars"""
    return [], [], True

def hover(posX, posY):
    """making hover effects"""
    if exitButton.checkMouse(posX, posY):
        exitButton.color = GREENHOVER
    else:
        exitButton.color = RED
    if overAllStatsButton.checkMouse(posX, posY):
        overAllStatsButton.color = GREENHOVER
    else:
        overAllStatsButton.color = RED
    if endButton.checkMouse(posX, posY):
        endButton.color = GREENHOVER
    else:
        endButton.color = RED

    if statsButton.checkMouse(posX, posY):
        statsButton.color = GREENHOVER
    else:
        statsButton.color = RED

    if timerButton.checkMouse(posX, posY):
        timerButton.color = GREENHOVER
    else:
        timerButton.color = RED

def overAllButton(overAll,state):
    """changing state of overAllButton"""
    if state == "OVER ALL STATS":
        state = "   DAILY    STATS"
        overAll = True
    else:
        state = "OVER ALL STATS"
        overAll = False
    return overAll, state

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
