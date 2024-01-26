import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from level import Level
from overworld import OverWorld


class Game:
    def __init__(self):
        pygame.init()
        # Screen Setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('PLATFORMER')
        pygame.display.set_icon(pygame.image.load('../graphics/64629c0ba19e223.png'))
        self.background = pygame.transform.scale(pygame.image.load(
            '../graphics/pixel-art-christmas-landscape-with-red-house-pine-snow-santa-claus-8-bit-game-background-vector.jpeg'),
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        self.clock = pygame.time.Clock()
        self.max_level = 2
        self.over_world = OverWorld(0, self.max_level, self.screen, self.create_level)
        self.status = 'over_world'

    def create_level(self, current_level):
        self.level = Level(self.screen, current_level, self.create_over_world)
        self.status = 'level'

    def create_over_world(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.over_world = OverWorld(current_level, self.max_level, self.screen, self.create_level)
        self.status = 'over_world'

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill((155, 155, 155))
        self.screen.blit(self.background, (0, 0))
        if self.status == 'over_world':
            self.over_world.run()
        else:
            self.level.run()
        pygame.display.update()

    def run(self):
        while True:
            self.input()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
