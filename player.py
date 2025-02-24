import pygame
import os

class Bear(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_sheet):
        super().__init__()
        self.x, self.y = x, y
        self.health = 100
        self.gold = 0
        self.speed = 4
        self.sprite_sheet = sprite_sheet
        self.load_sprites()
        self.current_sprite = self.sprites["idle"][0]
        self.rect = self.current_sprite.get_rect(topleft=(x, y))
        self.vel_x, self.vel_y = 0, 0
        self.facing_right = True
        self.animation_frame = 0

    def load_sprites(self):
        """Load different animations from the sprite sheet"""
        self.sprites = {
            "idle": [self.sprite_sheet.subsurface((0, 0, 32, 32))],  # Replace with actual coordinates
            "walk": [self.sprite_sheet.subsurface((32, 0, 32, 32))],  
            "attack": [self.sprite_sheet.subsurface((64, 0, 32, 32))],  
        }

    def handle_keydown(self, key):
        """Detect key press events and update movement."""
        if key == pygame.K_a:
            self.movement["left"] = True
        elif key == pygame.K_d:
            self.movement["right"] = True
        elif key == pygame.K_w:
            self.movement["up"] = True
        elif key == pygame.K_s:
            self.movement["down"] = True

    def handle_keyup(self, key):
        """Detect key release events and stop movement."""
        if key == pygame.K_a:
            self.movement["left"] = False
        elif key == pygame.K_d:
            self.movement["right"] = False
        elif key == pygame.K_w:
            self.movement["up"] = False
        elif key == pygame.K_s:
            self.movement["down"] = False

    def move(self, dx, dy):
        self.vel_x = dx * self.speed
        self.vel_y = dy * self.speed
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False

    def update(self):
        """Update player position based on key states."""
        self.vel_x = self.vel_y = 0  # Reset movement
        
        if self.movement["left"]:
            self.vel_x = -self.speed
            self.facing_right = False
        if self.movement["right"]:
            self.vel_x = self.speed
            self.facing_right = True
        if self.movement["up"]:
            self.vel_y = -self.speed
        if self.movement["down"]:
            self.vel_y = self.speed

        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.topleft = (self.x, self.y)

        # Update sprite animation
        if self.vel_x != 0 or self.vel_y != 0:
            self.animation_frame = (self.animation_frame + 1) % len(self.sprites["walk"])
            self.current_sprite = self.sprites["walk"][self.animation_frame]
        else:
            self.current_sprite = self.sprites["idle"][0]

    def draw(self, screen):
        if self.facing_right:
            screen.blit(self.current_sprite, self.rect.topleft)
        else:
            flipped_sprite = pygame.transform.flip(self.current_sprite, True, False)
            screen.blit(flipped_sprite, self.rect.topleft)

    def attack(self):
        """Basic attack logic"""
        self.animation_frame = 0
        self.current_sprite = self.sprites["attack"][0]

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        print("You Died!")  # Placeholder, we’ll add game over logic later


# WarriorBear class (inherits from Bear)
class WarriorBear(Bear):
    def __init__(self, x=100, y=100):
        sprite_sheet = pygame.image.load("assets/sprites/warrior_bear.png").convert_alpha()
        super().__init__(x, y, sprite_sheet)
        self.health = 150  # More health than other classes
        self.attack_power = 15

    def attack(self):
        super().attack()
        print("Warrior swings his axe!")  # Placeholder attack logic


# MageBear class (inherits from Bear)
class MageBear(Bear):
    def __init__(self, x=100, y=100):
        sprite_sheet = pygame.image.load("assets/sprites/mage_bear.png").convert_alpha()
        super().__init__(x, y, sprite_sheet)
        self.health = 80
        self.mana = 100
        self.attack_power = 10

    def attack(self):
        super().attack()
        if self.mana >= 10:
            self.mana -= 10
            print("Mage casts a fireball!")  # Placeholder attack logic
        else:
            print("Not enough mana!")


# ArcherBear class (inherits from Bear)
class ArcherBear(Bear):
    def __init__(self, x=100, y=100):
        sprite_sheet = pygame.image.load("assets/sprites/archer_bear.png").convert_alpha()
        super().__init__(x, y, sprite_sheet)
        self.health = 100
        self.arrows = 10
        self.attack_power = 12

    def attack(self):
        super().attack()
        if self.arrows > 0:
            self.arrows -= 1
            print("Archer fires an arrow!")  # Placeholder attack logic
        else:
            print("Out of arrows!")
