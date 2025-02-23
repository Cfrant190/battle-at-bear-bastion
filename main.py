import pygame, sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption("Battle at Bear Bastion")

    def run(self):
        while self.running:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0,0,0))
            pygame.display.flip()

        pygame.quit()
        sys.exit()
        pygame.display.update()

game = Game()
game.run()