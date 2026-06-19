import pygame

class Chicken(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load chicken image
        self.image = pygame.image.load("image/hen.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Default position (will be set later in spaceranger.py when spawning rows)
        self.rect.x = 0
        self.rect.y = 0

        # Movement speed (optional if you want chickens to move)
        self.speed = 1

    def update(self):
        # If you want chickens to move left/right, add logic here
        # Example: self.rect.x += self.speed
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
