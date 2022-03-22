"""Import modules"""
from functions import get_pos_mouse
from variables import *
from stats import *
from timer import *


def main_menu():
    """main menu"""
    playing = True
    while playing:
        screen.fill((255,255,255))
        #pos mouse
        pos_x, pos_y = get_pos_mouse()
        hover(pos_x, pos_y)

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
                if end_button.check_mouse(pos_x, pos_y):
                    playing = False
                elif stats_button.check_mouse(pos_x, pos_y):
                    playing = stats(True)
                elif timer_button.check_mouse(pos_x, pos_y):
                    playing = timer(True)
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
        stats_button.display()
        timer_button.display()
        end_button.display()
        screen.blit(menu_image, (width / 2 - 300 / 2, 100))
        pygame.display.flip()
    pygame.quit()