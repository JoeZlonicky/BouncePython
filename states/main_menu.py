import pygame
import states.playing
from state import State
from label import Label


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.title_label = Label("Bounce", 80)
        self.name_label = Label("By Joe Zlonicky", 64)
        self.prompt_label = Label("Press Anything to Start", 48)

        self.title_label.rect.center = (self.game.screen_size[0] / 2, 150)
        self.name_label.rect.center = (self.game.screen_size[0] / 2, 250)
        self.prompt_label.rect.center = (self.game.screen_size[0] / 2, 650)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.game.change_state(states.playing.Playing)

    def draw(self):
        for label in [self.title_label, self.name_label, self.prompt_label]:
            self.game.screen.blit(label.image, label.rect)
