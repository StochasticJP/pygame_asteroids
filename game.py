import pygame
from gameobject import GameObject
import utils

# class const
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        self._init_pygame()  # when this class is called - init pygame method is initialized
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = utils.load_sprite("space", False)
        self.spaceship = GameObject((400, 300), utils.load_sprite("spaceship"), (0, 0))
        self.asteroid = GameObject((400, 300), utils.load_sprite("asteroid"), (1, 0))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Game Asteroids")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # fills the screen with each frame
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        pygame.display.flip()  # updates the content of the screen

