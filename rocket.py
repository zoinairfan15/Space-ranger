import pygame

class Rocket(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load("image/rocket.png")
        self.rocket_rect = self.image.get_rect(midbottom=(400, 580))
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rocket_rect.right < 800:
            self.rocket_rect.x += 5
        if self.move_left and self.rocket_rect.left > 0:
            self.rocket_rect.x -= 5

    def blit_rocket(self):
        self.screen.blit(self.image, self.rocket_rect)

    def boundaries(self):
        if self.rocket_rect.left < 0:
            self.rocket_rect.left = 0
        if self.rocket_rect.right > 800:
            self.rocket_rect.right = 800

    def position_update(self):
        self.rocket_rect.midbottom = (400, 580)
