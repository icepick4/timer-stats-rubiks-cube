"""IMPORTING CLASSES"""
from datetime import datetime
import glob
import json
try:
    import pygame
except ModuleNotFoundError:
    print("""Vous n'avez pas téléchargé le module pygame
    ! \n Téléchargez le avec la commande ci-contre : pip install pygame"""
    )
from classes.button import Button
from classes.text import Text

RED = (255,50,50)
YELLOW = (255,215,0)
BLACK = (0,0,0)
GREY = (50,50,50)
WHITE = (255,255,255)
GREEN = (50,255,50)
GREENHOVER = (28, 184, 48)

#setting window
window_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(window_size)
width = window_size[0]
height = window_size[1]

date = datetime.today().strftime('%d-%m-%Y')
PLAYING = True
#####FONTS#####
FONTPATH = "assets/font/aAkhirTahun.ttf"
pygame.font.init()
font50 = pygame.font.Font(FONTPATH, 50)
font75 = pygame.font.Font(FONTPATH, 75)
font100 = pygame.font.Font(FONTPATH, 100)
font125 = pygame.font.Font(FONTPATH, 125)
font200 = pygame.font.Font(FONTPATH, 200)
font300 = pygame.font.Font(FONTPATH, 300)
font_width = pygame.font.Font(FONTPATH, int(width * 0.025))
#####MENU PAGE#####
#bouton pour fermer la fenetre
end_button = Button("CLOSE", font50, RED,(width - width / 10, 20))
stats_button = Button("STATS", font125, RED,(width / 2 - 400, height / 2 +100))
timer_button = Button("TIMER", font125, RED, (width/2 +150, height / 2 +100))
exit_button = Button("EXIT", font50, RED, (20,20))
menu_image = pygame.transform.smoothscale(
    pygame.image.load("assets/image/rubik's_cube.png").convert_alpha(),
    (380,400)
)
with open("data.json", "r", encoding = "utf-8") as f:
    data = json.load(f)
#####TIMER PAGE#####
timer_header = Text("SCRAMBLE : ", font75, BLACK, (width / 10 , 20))
list_of_cubes_paths = glob.glob("assets/image/cubes/*")
list_of_cubes = []
for path in list_of_cubes_paths:
    list_of_cubes.append([
                        pygame.transform.smoothscale(
                        pygame.image.load(path).convert_alpha(), (330,300))
                        ,
                        Text(
                            path[19:len(path)-4].replace("_"," "),
                            font75,
                            BLACK,
                            (width / 2, height /1.7)
                            )
                        ])
cubes_rect = pygame.Rect((width / 2 - 330 / 2, height / 1.5, 330,300))
chrono_text = font200.render(f"{0.00}", True, BLACK)
chrono_rect = chrono_text.get_rect(
                                midtop=(width/2 - chrono_text.get_width() / 4,
                                        height / 2 - chrono_text.get_height()
                                        )
                                )
remove_button = Button(
                     "REMOVE LAST TIME",
                     font_width,
                     RED,
                     (width - width / 3.5, height - 100)
                     )
LASTCHRONO = 0
#####STATS PAGE#####
over_all_stats_button = Button(
                            "OVER ALL STATS",
                            font50,
                            RED,
                            (width / 30, height - height / 10)
                            )
screen.fill((255,255,255))
