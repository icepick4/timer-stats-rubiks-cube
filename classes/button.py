"""Modules"""
import pygame
import variables

class Button:
    """INIT A BUTTON"""
    def __init__(self, text, font, color, pos):
        #text init
        self.font = font
        self.font_rect = font.render(text, True, color).get_rect(topleft = pos)
        #button init
        self.button_surface = pygame.Surface((self.font_rect.w * 1.2, self.font_rect.h * 1.2))
        self.button_rect = self.button_surface.get_rect(
                                                topleft = (
                                                    self.font_rect.left - self.font_rect.w * 0.1,
                                                    self.font_rect.top - self.font_rect.h * 0.15)
                                                )
        self.color = color
        self.text = text
    def display(self):
        """DISPLAY THE BUTTON"""
        pygame.draw.rect(variables.screen, variables.BLACK, self.button_rect, 3, border_radius = 20)
        variables.screen.blit(self.font.render(self.text, True, self.color),self.font_rect)

    def check_mouse(self, pos_x, pos_y):
        """RETURN TRUE IS MOUSE IN BUTTON, ELSE RETURN FALSE"""
        width_restriction = self.button_rect.left < pos_x < self.button_rect.right
        height_restriction = self.button_rect.top < pos_y < self.button_rect.bottom
        return width_restriction and height_restriction
