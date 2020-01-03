import pygame


class State:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def update(self):
        pass

    def draw(self):
        pass
