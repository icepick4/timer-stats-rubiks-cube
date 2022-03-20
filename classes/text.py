
class Text:
    def __init__(self, screen, text, font, color, pos):
        self.screen = screen
        self.text = text
        self.font = font
        self.color = color
        self.surface = self.font.render(self.text, True, self.color)
        self.pos = (pos[0] - self.surface.get_width() / 2, pos[1])
        self.rect = self.surface.get_rect(topleft=self.pos)

    def display(self):
        self.screen.blit(self.surface,self.rect)
