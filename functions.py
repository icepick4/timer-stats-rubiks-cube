"""functions"""
import pygame
from time import time
from variables import screen, height, width, BLACK, RED
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