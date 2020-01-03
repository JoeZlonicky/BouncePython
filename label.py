import pygame


class Label:
    font_name = "Agency FB"

    def __init__(self, text, font_size):
        self.font = pygame.font.SysFont(self.font_name, font_size)
        self.image = self.font.render(text, True, (255, 255, 255)).convert_alpha()
        self.rect = self.image.get_rect()

