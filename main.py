import pygame, sys
from settings import *
from level import Level
from player import WarriorBear

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption("Battle at Bear Bastion")
        
        self.current_stage = Level()
        
        # Create groups for easy updating
        self.updatable = pygame.sprite.Group()
        
        # Initialize the player and add to update group
        self.player = WarriorBear(100, 100)
        self.player.containers = (self.updatable,)
        self.updatable.add(self.player)

    def run(self):
        while self.running:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.player.handle_keydown(event.key)
                elif event.type == pygame.KEYUP:
                    self.player.handle_keyup(event.key)
                    
            self.player.handle_input()
            
            # Update game objects
            self.updatable.update()
            
            # Draw everything
            self.screen.fill((0, 0, 0))  # Clear screen
            self.updatable.draw(self.screen)  # Draw all updatable sprites
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":  
    game = Game()
    game.run()
