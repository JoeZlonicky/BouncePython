import pygame
import game


class Paddle(pygame.sprite.Sprite):
    speed = 8
    rotation_speed = 0.75
    rotation_limit = 30

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/paddle.png").convert_alpha()
        self.original = self.image.copy()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.bottom = game.Game.screen_size[1] - 10
        self.rect.centerx = game.Game.screen_size[0] / 2

        self.rotation = 0

    def update(self, ball):
        self.update_collisions(ball)
        self.handle_input()
        self.constrain_position()

    def update_collisions(self, ball):
        if self.rect.colliderect(ball.rect) and self.is_hitting_ball(ball):
                ball.bounce(self.rotation)
                while self.is_hitting_ball(ball):
                    ball.rect.y -= 1

    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.speed
            self.rotate(-self.rotation_speed)
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.speed
            self.rotate(self.rotation_speed)

    def constrain_position(self):
        self.rect.centerx = max(min(game.Game.screen_size[0], self.rect.centerx), 0)

    def rotate(self, degrees):
        center_x, center_y = self.rect.centerx, self.rect.centery
        self.rotation += degrees
        self.rotation = max(min(self.rotation_limit, self.rotation), -self.rotation_limit)
        self.image = pygame.transform.rotate(self.original, int(self.rotation))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)

    def is_hitting_ball(self, ball):
        return pygame.sprite.spritecollide(self, [ball], False, pygame.sprite.collide_mask)
