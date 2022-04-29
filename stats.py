"""MODULES"""
from time import time
import pygame
from functions import (
                    create_triangle_down,
                    create_triangle_left,
                    create_triangle_right,
                    create_triangle_up,
                    get_pos_mouse, hover,
                    reset_arrow_left,
                    reset_arrow_right,
                    to_minutes
)
from variables import (
                Text,
                font75,
                font200,
                width,
                height,
                BLACK,
                screen,
                data,
                font125,
                RED,
                GREEN,
                exit_button,
                over_all_stats_button,
                list_of_little_cubes
)
def over_all_stats(over_all,state):
    """changing state of over_all_stats_button text"""
    if state == "OVER ALL STATS":
        state = "   DAILY    STATS"
        over_all = True
    else:
        state = "OVER ALL STATS"
        over_all = False
    return over_all, state
def reset_var():
    """reset vars"""
    return [], [], True

def fill_dicos(dico, dico_bool, datas, current_cube):
    """fill the dicos of stats page (dates and scores) depending of over_all bool"""
    if not dico_bool["over_all"] and dico_bool["switched"]:
        for score in datas[current_cube.text]:
            date_text = Text(
                            score['date'].replace("-", "/"),
                            font75, BLACK,
                            (width - width / 7, height - 100)
                            )
            try:
                if dico["list_of_dates"][-1].text != score['date'].replace("-", "/"):
                    dico["list_of_dates"].append(date_text)
            except IndexError:
                dico["list_of_dates"].append(date_text)
            dico["list_of_scores"].append([date_text, float(score['time'])])
        dico_bool["switched"] = False
    elif dico_bool["over_all"] and dico_bool["switched"]:
        for score in datas[current_cube.text]:
            dico["list_of_scores"].append(float(score['time']))
        dico_bool["switched"] = False
    return dico

def give_stats(list_of_scores, list_of_dates, selected_date, over_all):
    """returning the stats of a list of scores"""
    if not over_all:
        total = 0
        ctr = 0
        best = 9999
        worst = 0
        for score in list_of_scores:
            if score[0].text == list_of_dates[selected_date].text:
                total+=round(score[1],2)
                ctr+=1
                if score[1] > worst:
                    worst = score[1]
                if score[1] < best:
                    best = score[1]
        avg = round(total / ctr,2)
    else:
        avg = round(sum(list_of_scores) / len(list_of_scores),2)
        best = min(list_of_scores)
        worst = max(list_of_scores)
    if avg > 60:
        avg = to_minutes(avg)
    if best > 60:
        best = to_minutes(best)
    if worst > 60:
        worst = to_minutes(worst)
    return avg, best, worst

def init_cube_stats(cubes):
    """init pos of cubes in stats page"""
    for cube in cubes:
        cube[1].rect = cube[1].surface.get_rect(
                                            topright=(
                                                    width -10,
                                                    10
                                                    )
                                            )
    return cubes

def create_arrows(over_all, state_date, timer_arrows):
    """creating all arrows on screen"""
    create_triangle_right(timer_arrows["timeArrowRight"])
    create_triangle_left(timer_arrows["timeArrowLeft"])
    if not over_all and state_date:
        create_triangle_down(timer_arrows["timeArrowDown"])
        create_triangle_up(timer_arrows["timeArrowUp"])

def stats(playing):
    """STATS PAGE"""
    timer_arrows = {
        "timeArrowLeft":time() - 0.1,
        "timeArrowRight" : time() - 0.1,
        "timeArrowUp" : time() - 0.1,
        "timeArrowDown" : time() - 0.1
    }
    dico = {
        "selectedCube":0,
        "selected_date":0,
        "list_of_scores": [],
        "list_of_dates":[]
    }
    dico_bool = {
        "over_all" : False,
        "switched" : True
    }
    cubes = init_cube_stats(list_of_little_cubes)
    while playing:
        current_cube = cubes[dico["selectedCube"]][1]
        screen.fill((255,255,255))
        dico = fill_dicos(dico, dico_bool, data, current_cube)
        #pos mouse
        pos_x, pos_y = get_pos_mouse()
        #####HOVER#####
        hover(pos_x, pos_y)
        #####ARROWS#####
        create_arrows(dico_bool["over_all"], len(dico["list_of_dates"]) > 1, timer_arrows)
        try:
            avg, best, worst = give_stats(dico["list_of_scores"],
                                         dico["list_of_dates"],
                                         dico["selected_date"],
                                         dico_bool["over_all"]
                                         )
            Text(
                f"Average : {avg}",
                font125, BLACK,
                (width / 2, height / 2.5 - 150)
            ).display()
            Text(
                f"Best : {best}",
                font125, GREEN,
                (width / 2, height / 2.5)
            ).display()
            Text(
                f"Worst : {worst}",
                font125,
                RED,
                (width / 2, height / 2.5 + 150)
            ).display()
            if not dico_bool["over_all"]:
                dico["list_of_dates"][dico["selected_date"]].display()
        except (ZeroDivisionError,IndexError):
            #if no data
            Text("No data", font200, BLACK, (width/2, height / 2.5)).display()
        for event in pygame.event.get():
            scroll_up = event.type == 1025 and event.button == 4
            scroll_down = event.type == 1026 and event.button == 5
            if event.type == 256:
                playing = False
            elif event.type == 1025 and event.button == 1 :
                if exit_button.check_mouse(pos_x, pos_y):
                    playing = False
                elif over_all_stats_button.check_mouse(pos_x, pos_y):
                    dico_bool["over_all"], over_all_stats_button.text = over_all_stats(
                                                            over_all_stats_button.text,
                                                            over_all_stats_button.text
                                                            )
                    dico["list_of_dates"],dico["list_of_scores"],dico_bool["switched"]=reset_var()
            elif event.type == 768 and event.key == 1073741904:
                #left
                dico["selectedCube"],timer_arrows["timeArrowLeft"] = reset_arrow_left(
                                                dico["selectedCube"],
                                                len(cubes)
                                                )
                dico["list_of_dates"],dico["list_of_scores"],dico_bool["switched"]=reset_var()
            elif event.type == 768 and event.key == 1073741903:
                #right
                dico["selectedCube"],timer_arrows["timeArrowRight"] = reset_arrow_right(
                                            dico["selectedCube"],
                                            len(cubes)
                                            )
                dico["list_of_dates"],dico["list_of_scores"],dico_bool["switched"]=reset_var()
            elif event.type == 768 and event.key == 1073741906 or scroll_up:
                #up
                dico["selected_date"],timer_arrows["timeArrowUp"] = reset_arrow_left(
                                            dico["selected_date"],
                                            len(dico["list_of_dates"])
                                            )
            elif (event.type == 768 and event.key == 1073741905) or scroll_down:
                #down
                dico["selected_date"],timer_arrows["timeArrowDown"] = reset_arrow_right(
                                            dico["selected_date"],
                                            len(dico["list_of_dates"])
                                            )
        cubes[dico["selectedCube"]][1].display()
        screen.blit(cubes[dico["selectedCube"]][0], (width - 150, 75))
        over_all_stats_button.display()
        exit_button.display()
        pygame.display.flip()
    return True
        