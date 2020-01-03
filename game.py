import pygame
import random
from states.main_menu import MainMenu


class Game:
    screen_size = (500, 800)
    backgrounds = [(242, 95, 72), (244, 153, 34), (196, 63, 244),
                   (67, 239, 118), (113, 90, 244)]

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Bounce")
        self.clock = pygame.time.Clock()
        self.background_number = random.randint(0, len(self.backgrounds) - 1)
        self.scores = []
        self.states = []
        self.current_state = MainMenu(self)
        self.load_scores()

    def loop(self):
        while True:
            self.handle_events()
            self.current_state.update()
            self.screen.fill(self.backgrounds[self.background_number])
            self.current_state.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.save_scores()
                exit()
        self.current_state.handle_events(events)

    def change_state(self, state_class):
        self.current_state = self.get_state(state_class)

    def get_state(self, state_class):
        for state in self.states:
            if isinstance(state, state_class):
                return state
        else:
            new_state = state_class(self)
            self.states.append(new_state)
            return new_state

    def save_scores(self):
        with open("scores.txt", "w") as file:
            for score in self.scores[0:5]:
                file.write(str(score) + "\n")

    def load_scores(self):
        try:
            with open("scores.txt", "r") as file:
                for val in file.read().split():
                    self.scores.append(int(val))
        except FileNotFoundError:
            return
