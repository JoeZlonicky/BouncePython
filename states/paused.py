import pygame
import states.playing
from state import State


class Paused(State):
    def __init__(self, game):
        super().__init__(game)
        self.pause_icon = pygame.image.load("assets/pause.png").convert_alpha()
        self.pause_rect = self.pause_icon.get_rect()
        self.pause_rect.center = (self.game.screen_size[0] / 2,
                                  self.game.screen_size[1] / 2)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_state(states.playing.Playing)

    def draw(self):
        self.game.get_state(states.playing.Playing).draw()
        self.game.screen.blit(self.pause_icon, self.pause_rect)