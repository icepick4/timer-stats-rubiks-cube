"""MODULES"""
from time import time
import pygame
from pygame.locals import *
from functions import to_minutes,get_pos_mouse,hover,create_triangle_right,create_triangle_left,reset_arrow_left, reset_arrow_right
# from variables import screen,font200, list_of_cubes, exit_button, remove_button, width, data, font75, font300, cubesRect, date, chronoRect, BLACK, RED, GREEN
from variables import *

def display_live_stats(chronos, last_chrono, cube):
    """display the stats in live on the right of the timer page"""
    if last_chrono != 0:
        if last_chrono > 60:
            last_chrono = to_minutes(last_chrono)
        last = font75.render(f"Last : {last_chrono}", True, BLACK)
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
            ao5 = to_minutes(ao5)
        ao5 = font75.render(f"ao5 : {ao5}", True, BLACK)
        screen.blit(ao5, (width / 1.3, 100))
    #update the current ao12
    if len(chronos) > 12:
        ao12 = round(sum(chronos[cube][len(chronos[cube]) - 12: len(chronos[cube])])/ 12, 2)
        if ao12 > 60:
            ao12 = to_minutes(ao12)
        ao12 = font75.render(f"ao12 : {ao12}", True, BLACK)
        screen.blit(ao12, (width / 1.3, 200))

def set_chrono(in_chrono, holding, start_holding, chrono):
    """set the chrono to display it right after"""
    if in_chrono:
        screen.fill((255,255,255))
        if float(chrono) > 60:
            chrono_minutes = to_minutes(chrono)
            text = font300.render(f"{chrono_minutes}", True, BLACK)
        else:
            text = font300.render(f"{chrono}", True, BLACK)
    elif holding and time() - start_holding < 0.5:
        text = font300.render(f"{chrono}", True, RED)
    elif holding and time() - start_holding > 0.5:
        screen.fill((255,255,255))
        text = font300.render("0.0", True, GREEN)
    else:
        if float(chrono) > 60:
            chrono_minutes = to_minutes(chrono)
            text = font300.render(f"{chrono_minutes}", True, BLACK)
        else:
            text = font300.render(f"{chrono}", True, BLACK)
    return text

def blits_timer(selected_cube):
    """blit on timer page"""
    exit_button.display()
    list_of_cubes[selected_cube][1].display()
    screen.blit(list_of_cubes[selected_cube][0], cubes_rect)
    remove_button.display()

def remove_last(list_of_data, index):
    """remove last time"""
    if len(list_of_data[index]) > 0:
        list_of_data[index].pop()
    return list_of_data

def update_chrono(in_chrono, current_cube, chrono, last_chronos):
    """update the chrono when finished"""
    if in_chrono:
        in_chrono = False
        data[current_cube].append({"time": chrono, "date":date})
        last_chronos[current_cube].append(float(chrono))
    return in_chrono, last_chronos

def update_live_chrono(in_chrono, start_time, cube):
    """update the chrono in live and last chrono"""
    try:
        last_chrono = cube[-1]
    except IndexError:
        last_chrono = 0.0
    if in_chrono:
        chrono = str(round(time() - start_time, 2))
    else:
        chrono = str(float(last_chrono))
    return chrono, last_chrono

def timer(playing):
    """TIMER PAGE"""
    screen.fill((255,255,255))
    start_time = time()
    timer_arrows = {
        "timeArrowLeft":time() - 0.1,
        "timeArrowRight" : time() - 0.1,
    }
    dico = {
        "in_chrono":False,
        "holding":False,
        "chrono": "0.0",
        "selected_cube": 0,
        "start_holding": 0
    }
    last_chronos = {
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
        current_cube = list_of_cubes[dico["selected_cube"]][1].text
        #pos mouse
        screen.fill((255,255,255))
        pos_x, pos_y = get_pos_mouse()
        #hover button
        hover(pos_x, pos_y)
        create_triangle_right(timer_arrows["timeArrowRight"])
        create_triangle_left(timer_arrows["timeArrowLeft"])
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
                #checking for button pressed
                if exit_button.check_mouse(pos_x, pos_y):
                    playing = False
                if remove_button.check_mouse(pos_x, pos_y):
                    last_chronos = remove_last(last_chronos, current_cube)
                    remove_last(data, current_cube)
            #choose the cube you want
            elif event.type == KEYDOWN and event.key == K_LEFT:
                dico["selected_cube"], timer_arrows["timeArrowLeft"] = reset_arrow_left(
                                                                        dico["selected_cube"],
                                                                        len(list_of_cubes)
                                                                        )
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                dico["selected_cube"], timer_arrows["timeArrowRight"] = reset_arrow_right(
                                                                        dico["selected_cube"],
                                                                        len(list_of_cubes)
                                                                        )
            elif event.type == KEYDOWN and event.key == K_SPACE:
                dico["in_chrono"], last_chronos = update_chrono(
                                                            dico["in_chrono"],
                                                            current_cube,
                                                            dico["chrono"],
                                                            last_chronos
                                                            )
                dico["start_holding"] = time()
                dico["holding"] = True
            elif event.type == KEYUP and event.key == K_SPACE:
                #chekc holding enought time
                if time() - dico["start_holding"] > 0.5:
                    dico["in_chrono"] = True
                    start_time = time()
                else:
                    dico["holding"] = False
        #update dict of last_chronos and chrono
        dico["chrono"], last_chrono = update_live_chrono(
                                                    dico["in_chrono"],
                                                    start_time,
                                                    last_chronos[current_cube]
                                                    )
        #update the last score
        #####DISPLAYS#####
        display_live_stats(last_chronos, last_chrono, current_cube)
        blits_timer(dico["selected_cube"])
        text = set_chrono(dico["in_chrono"],
                                dico["holding"],
                                dico["start_holding"],
                                dico["chrono"]
                                )
        screen.blit(text, chrono_rect)
        pygame.display.flip()
    return True
