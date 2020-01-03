import pygame
import random
import game


class Gem(pygame.sprite.Sprite):
    diamond_chance = 20

    def __init__(self):
        super().__init__()
        self.is_diamond = self.determine_if_diamond()
        image = "assets/yellow_gem.png" if self.is_diamond else "assets/gem.png"
        self.image = pygame.image.load(image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.get_random_location()
        self.value = 3 if self.is_diamond else 1

    def is_hit(self, ball):
        if self.rect.colliderect(ball.rect) and self.is_hitting_ball(ball):
            return True
        return False

    def is_hitting_ball(self, ball):
        return pygame.sprite.spritecollide(self, [ball], False, pygame.sprite.collide_mask)

    @staticmethod
    def get_random_location():
        x_range = [30, game.Game.screen_size[0] - 30]
        y_range = [300, game.Game.screen_size[1] - 200]
        return random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])

    def determine_if_diamond(self):
        roll = random.randint(1, 100)
        if self.diamond_chance > roll:
            return True
        return False
