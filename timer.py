"""MODULES"""
from time import time
import pygame
from pygame.locals import *
from functions import toMinutes,getPosMouse,hover,createTriangleRight,createTriangleLeft,resetArrowLeft, resetArrowRight
# from variables import screen,font200, listOfCubes, exitButton, removeButton, width, data, font75, font300, cubesRect, date, chronoRect, BLACK, RED, GREEN
from variables import *

def displayLiveStats(chronos, lastChrono, cube):
    """display the stats in live on the right of the timer page"""
    if lastChrono != 0:
        if lastChrono > 60:
            lastChrono = toMinutes(lastChrono)
        last = font75.render(f"Last : {lastChrono}", True, BLACK)
        screen.blit(last, (width - last.get_width() - 20, 10))
    #update the current
    if len(chronos[cube]) > 5:
        ao5 = round(
                    sum(
                        chronos[cube][len(chronos[cube]) - 5: len(chronos[cube])]
                        )/ 5,
                    2
                    )
        if ao5 > 60:
            ao5 = toMinutes(ao5)
        ao5 = font75.render(f"ao5 : {ao5}", True, BLACK)
        screen.blit(ao5, (width / 1.3, 100))
    #update the current ao12
    if len(chronos) > 12:
        ao12 = round(sum(chronos[cube][len(chronos[cube]) - 12: len(chronos[cube])])/ 12, 2)
        if ao12 > 60:
            ao12 = toMinutes(ao12)
        ao12 = font75.render(f"ao12 : {ao12}", True, BLACK)
        screen.blit(ao12, (width / 1.3, 200))

def setChrono(inChrono, holding, startHolding, chrono):
    """set the chrono to display it right after"""
    if inChrono:
        screen.fill((255,255,255))
        if float(chrono) > 60:
            chronoMinutes = toMinutes(chrono)
            text = font300.render(f"{chronoMinutes}", True, BLACK)
        else:
            text = font300.render(f"{chrono}", True, BLACK)
    elif holding and time() - startHolding < 0.5:
        text = font300.render(f"{chrono}", True, RED)
    elif holding and time() - startHolding > 0.5:
        screen.fill((255,255,255))
        text = font300.render("0.0", True, GREEN)
    else:
        if float(chrono) > 60:
            chronoMinutes = toMinutes(chrono)
            text = font300.render(f"{chronoMinutes}", True, BLACK)
        else:
            text = font300.render(f"{chrono}", True, BLACK)
    return text

def blitsTimer(selectedCube):
    """blit on timer page"""
    exitButton.display()
    listOfCubes[selectedCube][1].display()
    screen.blit(listOfCubes[selectedCube][0], cubesRect)
    removeButton.display()

def removeLast(list, index):
    """remove last time"""
    if len(list[index]) > 0:
        list[index].pop()
    return list

def updateChrono(inChrono, currentCube, chrono, lastChronos):
    """update the chrono when finished"""
    if inChrono:
        inChrono = False
        data[currentCube].append({"time": chrono, "date":date})
        lastChronos[currentCube].append(float(chrono))
    return inChrono, lastChronos

def updateLiveChrono(inChrono, startTime, cube):
    """update the chrono in live and last chrono"""
    try:
        lastChrono = cube[-1]
    except IndexError:
        lastChrono = 0.0
    if inChrono:
        chrono = str(round(time() - startTime, 2))
    else:
        chrono = str(float(lastChrono))
    return chrono, lastChrono

def timer(playing):
    """TIMER PAGE"""
    screen.fill((255,255,255))
    startTime = time()
    timerArrows = {
        "timeArrowLeft":time() - 0.1,
        "timeArrowRight" : time() - 0.1,
    }
    dico = {
        "inChrono":False,
        "holding":False,
        "chrono": "0.0",
        "selectedCube": 0,
        "startHolding": 0
    }
    lastChronos = {
    "2x2": [],
    "3x3": [],
    "4x4": [],
    "5x5": [],
    "6x6": [],
    "7x7": [],
    "megaminx": [],
    "mirror 3x3": [],
    "mirror 4x4": [],
    "mirror 5x5": [],
    "pyraminx": [],
    "skewb": []
}
    while playing:
        #the current cube
        currentCube = listOfCubes[dico["selectedCube"]][1].text
        #pos mouse
        screen.fill((255,255,255))
        posX, posY = getPosMouse()
        #hover button
        hover(posX, posY)
        createTriangleRight(timerArrows["timeArrowRight"])
        createTriangleLeft(timerArrows["timeArrowLeft"])
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                #checking for button pressed
                if exitButton.checkMouse(posX, posY):
                    playing = False
                if removeButton.checkMouse(posX, posY):
                    lastChronos = removeLast(lastChronos, currentCube)
                    removeLast(data, currentCube)
            #choose the cube you want
            elif event.type == KEYDOWN and event.key == K_LEFT:
                dico["selectedCube"], timerArrows["timeArrowLeft"] = resetArrowLeft(
                                                                        dico["selectedCube"],
                                                                        len(listOfCubes)
                                                                        )
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                dico["selectedCube"], timerArrows["timeArrowRight"] = resetArrowRight(
                                                                        dico["selectedCube"],
                                                                        len(listOfCubes)
                                                                        )
            elif event.type == KEYDOWN and event.key == K_SPACE:
                dico["inChrono"], lastChronos = updateChrono(
                                                            dico["inChrono"],
                                                            currentCube,
                                                            dico["chrono"],
                                                            lastChronos
                                                            )
                dico["startHolding"] = time()
                dico["holding"] = True
            elif event.type == KEYUP and event.key == K_SPACE:
                #chekc holding enought time
                if time() - dico["startHolding"] > 0.5:
                    dico["inChrono"] = True
                    startTime = time()
                else:
                    dico["holding"] = False
        #update dict of lastchronos and chrono
        dico["chrono"], lastChrono = updateLiveChrono(
                                                    dico["inChrono"],
                                                    startTime,
                                                    lastChronos[currentCube]
                                                    )
        #update the last score
        #####DISPLAYS#####
        displayLiveStats(lastChronos, lastChrono, currentCube)
        blitsTimer(dico["selectedCube"])
        text = setChrono(dico["inChrono"],
                                dico["holding"],
                                dico["startHolding"],
                                dico["chrono"]
                                )
        screen.blit(text, chronoRect)
        pygame.display.flip()
    return True
