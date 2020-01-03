import pygame


class Particle:

    def __init__(self, size, x, y):
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        radius = int(self.size / 2)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
