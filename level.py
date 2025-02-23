from settings import *


class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def run(self):
        self.screen.fill((0,0,0))