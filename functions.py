"""functions"""
from time import time
import pygame
from variables import screen, height, width, BLACK, RED, font75, Text, exitButton, overAllStatsButton, GREENHOVER, endButton, statsButton, timerButton, removeButton

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

def getPosMouse():
    posMouse = pygame.mouse.get_pos()
    return (posMouse[0], posMouse[1])

def resetArrowLeft(selection, length):
    """reset an arrow"""
    if selection-1 > - length:
        selection -=1
    else:
        selection = 0
    return selection, time()

def resetArrowRight(selection, length):
    """reset an arrow"""
    if selection+1 < length:
        selection +=1
    else:
        selection = 0
    print(selection)
    return selection, time()

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
    if removeButton.checkMouse(posX, posY):
        removeButton.color = GREENHOVER
    else:
        removeButton.color = RED
