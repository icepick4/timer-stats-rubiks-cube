"""MODULES"""
from time import time
from functions import (
                    to_minutes,
                    get_pos_mouse,
                    hover,
                    create_triangle_mid_right,
                    create_triangle_mid_left,
                    reset_arrow_left,
                    reset_arrow_right
)
from variables import (
                font50,
                font300,
                width,
                BLACK,
                list_of_cubes,
                screen,
                data,
                RED,
                GREEN,
                exit_button,
                pygame,
                remove_button,
                cubes_rect,
                date,
                chrono_rect
)

def display_live_stats(chronos, last_chrono, cube):
    """display the stats in live on the right of the timer page"""
    if len(chronos[cube]) > 0:
        #display the number of chronos
        text = font50.render(f"Counter : {len(chronos[cube])}", True, BLACK)
        screen.blit(text, (width - text.get_width() - 10, 10))
        #update the current average
        average = round(sum(chronos[cube])/ len(chronos[cube]), 2)
        if average > 60:
            average = to_minutes(average)
        average = font50.render(f"AVG : {average}", True, BLACK)
        screen.blit(average, (width - average.get_width() - 10, 75))
    else:
        text = font50.render("Start playing", True, BLACK)
        text2 = font50.render("to see live stats", True, BLACK)
        screen.blit(text, (width - text.get_width() - 10, 10))
        screen.blit(text2, (width - text2.get_width() - 10, 60))
    #update current lastscore
    if last_chrono != 0:
        if last_chrono > 60:
            last_chrono = to_minutes(last_chrono)
        last = font50.render(f"Last : {last_chrono}", True, BLACK)
        screen.blit(last, (width - last.get_width() - 10, 140))
    #update the current ao5
    if len(chronos[cube]) > 4:
        ao5 = round(
                    sum(
                        chronos[cube][len(chronos[cube]) - 5: len(chronos[cube])]
                        )/ 5,
                    2
                    )
        if ao5 > 60:
            ao5 = to_minutes(ao5)
        ao5 = font50.render(f"ao5 : {ao5}", True, BLACK)
        screen.blit(ao5, (width - ao5.get_width() - 10, 205))
    #update the current ao12
    if len(chronos[cube]) > 11:
        ao12 = round(sum(chronos[cube][len(chronos[cube]) - 12: len(chronos[cube])])/ 12, 2)
        if ao12 > 60:
            ao12 = to_minutes(ao12)
        ao12 = font50.render(f"ao12 : {ao12}", True, BLACK)
        screen.blit(ao12, (width - ao12.get_width() - 10, 270))

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

def blits_timer(selected_cube, last_chronos):
    """blit all stuff on timer page"""
    exit_button.display()
    list_of_cubes[selected_cube][1].display()
    screen.blit(list_of_cubes[selected_cube][0], cubes_rect)
    if len(last_chronos) > 0:
        remove_button.display()

def remove_last(list_of_data, index):
    """remove last time from data json or last_chronos array"""
    if len(list_of_data[index]) > 0:
        list_of_data[index].pop()
    return list_of_data

def update_chrono(in_chrono, current_cube, chrono, last_chronos):
    """update the lastchronos array when finished"""
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

def timer(looping):
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
    while looping:
        #the current cube
        current_cube = list_of_cubes[dico["selected_cube"]][1].text
        #pos mouse
        screen.fill((255,255,255))
        pos_x, pos_y = get_pos_mouse()
        #hover buttons
        hover(pos_x, pos_y)
        #create arrows
        create_triangle_mid_right(timer_arrows["timeArrowRight"])
        create_triangle_mid_left(timer_arrows["timeArrowLeft"])
        for event in pygame.event.get():
            if event.type == 256:
                looping = False
            elif event.type == 1025 and event.button == 1 :
                #checking for button pressed
                if exit_button.check_mouse(pos_x, pos_y):
                    looping = False
                if remove_button.check_mouse(pos_x, pos_y):
                    last_chronos = remove_last(last_chronos, current_cube)
                    remove_last(data, current_cube)
            #choose the cube you want
            elif event.type == 768 and event.key == 1073741904:
                dico["selected_cube"], timer_arrows["timeArrowLeft"] = reset_arrow_left(
                                                                        dico["selected_cube"],
                                                                        len(list_of_cubes)
                                                                        )
            elif event.type == 768 and event.key == 1073741903:
                dico["selected_cube"], timer_arrows["timeArrowRight"] = reset_arrow_right(
                                                                        dico["selected_cube"],
                                                                        len(list_of_cubes)
                                                                        )
            elif event.type == 768 and event.key == 32:
                dico["in_chrono"], last_chronos = update_chrono(
                                                            dico["in_chrono"],
                                                            current_cube,
                                                            dico["chrono"],
                                                            last_chronos
                                                            )
                dico["start_holding"] = time()
                dico["holding"] = True
            elif event.type == 769 and event.key == 32:
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
        blits_timer(dico["selected_cube"], last_chronos[current_cube])
        text = set_chrono(dico["in_chrono"],
                                dico["holding"],
                                dico["start_holding"],
                                dico["chrono"]
                                )
        screen.blit(text, chrono_rect)
        pygame.display.flip()
    return True
