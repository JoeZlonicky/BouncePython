import pygame
import states.playing
from state import State
from label import Label


class GameOver(State):
    score_spacing = 20

    def __init__(self, game):
        super().__init__(game)
        self.game_over_label = Label("Game Over", 80)
        self.high_score_label = Label("High Scores", 64)
        self.game_over_label.rect.center = (self.game.screen_size[0] / 2, 100)
        self.high_score_label.rect.center = (self.game.screen_size[0] / 2, 250)
        self.score_labels = []

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.game.change_state(states.playing.Playing)

    def draw(self):
        for label in [self.game_over_label, self.high_score_label] + self.score_labels:
            self.game.screen.blit(label.image, label.rect)

    def create_high_scores(self):
        self.score_labels[:] = []
        self.game.scores.sort(reverse=True)
        y = 325
        for i in range(5):
            if i > len(self.game.scores) - 1:
                break
            score = self.game.scores[i]
            new_label = Label(str(i + 1) + ": " + str(score), 48)
            new_label.rect.center = (self.game.screen_size[0] / 2, y)
            self.score_labels.append(new_label)
            y += self.score_spacing + new_label.image.get_height()
