import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load laser image
        self.image = pygame.image.load("image/laser.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Position laser at rocket’s current location
        self.rect.midtop = game.rocket.rocket_rect.midtop

        # Speed of laser
        self.speed = -8  # negative because it moves upward

    def update(self):
        # Move the laser upward
        self.rect.y += self.speed

    def draw(self, screen):
        # Draw laser on screen
        screen.blit(self.image, self.rect)
