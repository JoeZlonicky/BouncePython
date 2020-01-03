import pygame
import math
import game


class Ball(pygame.sprite.Sprite):
    gravity = 0.5
    max_velocity = 20.0
    bounce_strength = 25

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/ball.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.top = 10
        self.rect.centerx = game.Game.screen_size[0] / 2
        self.pos = [float(self.rect.x), float(self.rect.y)]
        self.velocity = [0.0, 0.0]

    def update(self):
        self.velocity[1] += self.gravity
        if self.velocity[1] > self.max_velocity:
            self.velocity[1] = self.max_velocity
        if self.rect.right > game.Game.screen_size[0]:
            self.rect.right = game.Game.screen_size[0]
            self.pos[0] = self.rect.left
            self.velocity[0] *= -1
        elif self.rect.left < 0:
            self.pos[0] = 0.0
            self.velocity[0] *= -1
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.update_rect()

    def update_rect(self):
        self.rect.x, self.rect.y = int(self.pos[0]), int(self.pos[1])

    def bounce(self, rotation):
        angle_rad = math.radians(rotation - 90)
        self.velocity[1] = math.sin(angle_rad) * self.bounce_strength
        self.velocity[0] = -math.cos(angle_rad) * self.bounce_strength
