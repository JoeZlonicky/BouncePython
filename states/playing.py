import pygame
import states.paused
import states.game_over
from state import State
from sprites.ball import Ball
from sprites.gem import Gem
from sprites.paddle import Paddle
from trail_handler import TrailHandler
from label import Label


class Playing(State):

    def __init__(self, game):
        super().__init__(game)
        self.ball = Ball()
        self.paddle = Paddle()
        self.gem = Gem()
        self.trail_handler = TrailHandler()
        self.score = 0
        self.score_label = None
        self.update_score_label()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_state(states.paused.Paused)

    def update(self):
        self.check_for_game_over()
        self.trail_handler.update(self.ball)
        self.ball.update()
        self.paddle.update(self.ball)
        self.check_for_point()

    def draw(self):
        for particle in self.trail_handler.particles:
            self.game.screen.blit(particle.image, particle.rect)
        for sprite in [self.ball, self.paddle, self.gem, self.gem, self.score_label]:
            self.game.screen.blit(sprite.image, sprite.rect)

    def check_for_game_over(self):
        if self.ball.rect.bottom > self.game.screen_size[1] * 2:
            self.game.scores.append(self.score)
            self.ball = Ball()
            self.paddle = Paddle()
            self.gem = Gem()
            self.score = 0
            self.update_score_label()
            self.game.get_state(states.game_over.GameOver).create_high_scores()
            self.game.change_state(states.game_over.GameOver)

    def check_for_point(self):
        if self.gem.is_hit(self.ball):
            self.score += self.gem.value
            self.update_score_label()
            self.next_background()
            self.gem = Gem()

    def next_background(self):
        self.game.background_number += 1
        if self.game.background_number > len(self.game.backgrounds) - 1:
            self.game.background_number = 0

    def update_score_label(self):
        self.score_label = Label(str(self.score), 64)
        self.score_label.rect.center = (self.game.screen_size[0] / 2, 30)
