import pygame
class Button:
    def __init__(self, screen, text, font, bgColor, color, pos):
        #text init
        self.font = font
        self.fontSurface = font.render(text, True, color)
        self.fontRect = self.fontSurface.get_rect(topleft = pos)

        #button init
        self.buttonSurface = pygame.Surface((self.fontRect.w * 1.2, self.fontRect.h * 1.2))
        self.buttonRect = self.buttonSurface.get_rect(topleft = (self.fontRect.left - self.fontRect.w * 0.1, self.fontRect.top - self.fontRect.h * 0.05))

        self.pos = pos
        self.screen = screen
        self.bgColor = bgColor
        self.color = color
        self.text = text

    def display(self):             
        pygame.draw.rect(self.screen, self.bgColor, self.buttonRect)
        self.fontSurface = self.font.render(self.text, True, self.color)
        self.screen.blit(self.fontSurface,self.fontRect)

    def checkMouse(self, posX, posY):
        return self.buttonRect.left < posX < self.buttonRect.right and self.buttonRect.top < posY < self.buttonRect.bottom

    
