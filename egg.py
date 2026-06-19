import pygame

class Egg(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        super().__init__()
        self.screen = game.screen

        # Load egg image
        self.image = pygame.image.load("image/egg.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Position egg at chicken’s location
        self.rect.x = pos_x
        self.rect.y = pos_y

        # Speed of falling egg
        self.speed = 5

    def update(self):
        # Move egg downward
        self.rect.y += self.speed

    def draw(self, screen):
        # Draw egg on screen
        screen.blit(self.image, self.rect)
