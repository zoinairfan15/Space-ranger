# spaceranger.py
import sys
import asyncio
import pygame
from rocket import Rocket
from laser import Laser
from chicken import Chicken
from egg import Egg

class SpaceRanger:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("SPACE RANGER")
        self.clock = pygame.time.Clock()

        self.rocket = Rocket(self)
        self.laser = pygame.sprite.Group()
        self.chicken = pygame.sprite.Group()
        self.egg = pygame.sprite.Group()

        self.attack = True
        self.rocket_life = 5
        self.game_not_over = False
        self.text_font = pygame.font.Font(None, 35)
        self.game_score = 0
        self.high_score = 0

        self.hit_timer = 0  # replaces sleep()

        # Sounds
        try:
            self.laser_sound = pygame.mixer.Sound("sound1/laser.wav")
            self.chicken_sound = pygame.mixer.Sound("sound1/chicken.wav")
            self.rocket_hit_sound = pygame.mixer.Sound("sound1/rocket_hit.wav")
        except:
            self.laser_sound = None
            self.chicken_sound = None
            self.rocket_hit_sound = None

        # Title screen
        self.title_image = pygame.image.load("image/title.png").convert_alpha()
        self.title_rect = self.title_image.get_rect(topleft=(0, 0))

    async def run_game(self):
        while True:
            if self.hit_timer > 0:
                self.hit_timer -= 1
                self._update_screen()
                self.clock.tick(60)
                await asyncio.sleep(0)
                continue

            if self.game_not_over:
                self._check_event()
                self._laser_update()
                self._time()
                self._egg_update()
            else:
                self.game_score = 0
                self.rocket_life = 5
                self.attack = True
                self.rocket.position_update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        self.game_not_over = True
                        self.chicken.empty()
                        self._chicken()

            self._update_screen()
            self.clock.tick(60)
            await asyncio.sleep(0)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.rocket.move_right = True
                elif event.key == pygame.K_a:
                    self.rocket.move_left = True
                elif event.key == pygame.K_SPACE:
                    self._laser_fire()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.rocket.move_right = False
                elif event.key == pygame.K_a:
                    self.rocket.move_left = False

    def _laser_fire(self):
        new_laser = Laser(self)
        self.laser.add(new_laser)
        if self.laser_sound:
            self.laser_sound.play()

    def _laser_update(self):
        for laser in self.laser.copy():
            if laser.rect.bottom <= 0:
                self.laser.remove(laser)
        self._collision_of_laser_chicken()

    def _collision_of_laser_chicken(self):
        collision = pygame.sprite.groupcollide(self.chicken, self.laser, True, True)
        if collision:
            self.game_score += 50
            if self.chicken_sound:
                self.chicken_sound.play()
        if not self.chicken:
            self.egg.empty()
            self.laser.empty()
            self._chicken()
            self.attack = True
            self.hit_timer = 30

    def _chicken(self):
        rows, cols = 3, 6
        for row in range(rows):
            for col in range(cols):
                chicken = Chicken(self)
                w, h = chicken.rect.size
                chicken.rect.x = w + 2 * w * col
                chicken.rect.y = h + 2 * h * row
                self.chicken.add(chicken)

    def _time(self):
        current_time = pygame.time.get_ticks() // 1000
        if current_time % 3 == 0:
            self._egg()

    def _egg(self):
        for chicken in self.chicken.sprites():
            if chicken.rect.x - 15 <= self.rocket.rocket_rect.x <= chicken.rect.x + 15 and self.attack:
                egg = Egg(self, chicken.rect.x, chicken.rect.y)
                self.egg.add(egg)
                self.attack = False
                break

    def _egg_update(self):
        for egg in self.egg.copy():
            if egg.rect.bottom >= 600:
                self.egg.remove(egg)
                self.attack = True
            if egg.rect.colliderect(self.rocket.rocket_rect):
                self._rocket_hit()
                break

    def _rocket_hit(self):
        if self.rocket_life > 0:
            self.rocket_life -= 1
            if self.rocket_hit_sound:
                self.rocket_hit_sound.play()
            self.egg.empty()
            self.laser.empty()
            self.attack = True
            self.hit_timer = 30
        if self.rocket_life == 0:
            self.chicken.empty()
            self._chicken()
            self.game_not_over = False

    def _dash_board(self):
        score = self.text_font.render(f"SCORE {self.game_score}", True, (60, 60, 60))
        life = self.text_font.render(f"LIFE {self.rocket_life}", True, (60, 60, 60))
        high = self.text_font.render(f"HIGH SCORE {self.high_score}", True, (60, 60, 60))
        self.screen.blit(score, (350, 20))
        self.screen.blit(life, (650, 20))
        self.screen.blit(high, (50, 20))
        if self.game_score > self.high_score:
            self.high_score = self.game_score

    def _update_screen(self):
        self.screen.fill("white")
        self.rocket.blit_rocket()
        self._dash_board()
        self.laser.draw(self.screen)
        self.laser.update()
        self.chicken.draw(self.screen)
        self.chicken.update()
        self.egg.draw(self.screen)
        self.egg.update()
        self.rocket.boundaries()
        self.rocket.update()
        if not self.game_not_over:
            self.screen.blit(self.title_image, self.title_rect)
        pygame.display.update()


async def main():
    sr = SpaceRanger()
    await sr.run_game()

asyncio.run(main())
