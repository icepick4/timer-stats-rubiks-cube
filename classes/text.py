"""class text"""
import pygame
pygame.init()
window_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(window_size)
class Text:
    """init a button"""
    def __init__(self, text, font, color, pos):
        self.screen = screen
        self.text = text
        self.font = font
        self.color = color
        self.surface = self.font.render(self.text, True, self.color)
        self.pos = (pos[0] - self.surface.get_width() / 2, pos[1])
        self.rect = self.surface.get_rect(topleft=self.pos)

    def display(self):
        """displaying the text"""
        screen.blit(self.surface,self.rect)

    def get_text(self):
        """get the text content"""
        return self.text
