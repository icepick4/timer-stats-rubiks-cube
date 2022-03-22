"""functions"""
from time import time
import pygame
from variables import (
                    screen,
                    height,
                    width,
                    BLACK,
                    RED,
                    exit_button,
                    over_all_stats_button,
                    GREENHOVER,
                    end_button,
                    stats_button,
                    timer_button,
                    remove_button
)

def to_minutes(chrono):
    """convert seconds to minute display"""
    return f"{int(float(chrono)/60)}:{round(float(chrono) - (float(chrono) // 60) * 60, 2)}"

def create_triangle_left(timer):
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

def create_triangle_mid_left(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                                screen,
                                BLACK,
                                [(width / 2 - 300,
                                height / 1.2),
                                (width / 2 - 200,
                                height / 1.3),
                                (width / 2 - 200, height / 1.1)]
                            )
    else:
        pygame.draw.polygon(
                                screen,
                                RED,
                                [(width / 2 - 300,
                                height / 1.2),
                                (width / 2 - 200,
                                height / 1.3),
                                (width / 2 - 200, height / 1.1)]
                            )

def create_triangle_mid_right(timer):
    """draw top arrow"""
    if time() - timer > 0.1:
        pygame.draw.polygon(
                                screen,
                                BLACK,
                                [(width / 2 + 300,
                                height / 1.2),
                                (width / 2 + 200,
                                height / 1.3),
                                (width / 2 + 200, height / 1.1)]
                            )
    else:
        pygame.draw.polygon(
                                screen,
                                RED,
                                [(width / 2 + 300,
                                height / 1.2),
                                (width / 2 + 200,
                                height / 1.3),
                                (width / 2 + 200, height / 1.1)]
                            )

def create_triangle_right(timer):
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

def create_triangle_up(timer):
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

def create_triangle_down(timer):
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

def get_pos_mouse():
    """return pos of mouse"""
    pos_mouse = pygame.mouse.get_pos()
    return (pos_mouse[0], pos_mouse[1])

def reset_arrow_left(selection, length):
    """reset an arrow"""
    if selection-1 > - length:
        selection -=1
    else:
        selection = 0
    return selection, time()

def reset_arrow_right(selection, length):
    """reset an arrow"""
    if selection+1 < length:
        selection +=1
    else:
        selection = 0
    return selection, time()

def hover(pos_x, pos_y):
    """making hover effects"""
    if exit_button.check_mouse(pos_x, pos_y):
        exit_button.color = GREENHOVER
    else:
        exit_button.color = RED
    if over_all_stats_button.check_mouse(pos_x, pos_y):
        over_all_stats_button.color = GREENHOVER
    else:
        over_all_stats_button.color = RED
    if end_button.check_mouse(pos_x, pos_y):
        end_button.color = GREENHOVER
    else:
        end_button.color = RED

    if stats_button.check_mouse(pos_x, pos_y):
        stats_button.color = GREENHOVER
    else:
        stats_button.color = RED

    if timer_button.check_mouse(pos_x, pos_y):
        timer_button.color = GREENHOVER
    else:
        timer_button.color = RED
    if remove_button.check_mouse(pos_x, pos_y):
        remove_button.color = GREENHOVER
    else:
        remove_button.color = RED
