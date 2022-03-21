"""Modules"""
import pygame
import variables
class Button:
    """INIT A BUTTON"""
    def __init__(self, text, font, color, pos):
        #text init
        self.font = font
        self.fontRect = font.render(text, True, color).get_rect(topleft = pos)
        #button init
        self.buttonSurface = pygame.Surface((self.fontRect.w * 1.2, self.fontRect.h * 1.2))
        self.buttonRect = self.buttonSurface.get_rect(
                                                    topleft = (
                                                        self.fontRect.left - self.fontRect.w * 0.1,
                                                        self.fontRect.top - self.fontRect.h * 0.15)
                                                    )
        self.color = color
        self.text = text
    def display(self):
        """DISPLAY THE BUTTON"""
        pygame.draw.rect(variables.screen, variables.BLACK, self.buttonRect, 3, border_radius = 20)
        variables.screen.blit(self.font.render(self.text, True, self.color),self.fontRect)

    def checkMouse(self, posX, posY):
        """RETURN TRUE IS MOUSE IN BUTTON, ELSE RETURN FALSE"""
        return self.buttonRect.left < posX < self.buttonRect.right and self.buttonRect.top < posY < self.buttonRect.bottom
