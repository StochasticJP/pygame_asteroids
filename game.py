import pygame
from gameobject import GameObject
from player import Player
import utils

class Game:
    # class const
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self):
        self._init_pygame()  # when this class is called - init pygame method is initialized
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background = utils.load_sprite("space", False)
        self.spaceship = Player((400, 300))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Game Asteroids")

    def _handle_input(self):
        # Player input handling
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        elif is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()

        # Handle input to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()



    def _process_game_logic(self):
        self.spaceship.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # fills the screen with each frame
        self.spaceship.draw(self.screen)
        pygame.display.flip()  # updates the content of the screen
        self.clock.tick(60)  # will wait it match the desired FPS

