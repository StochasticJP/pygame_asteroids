import pygame
from gameobject import GameObject
from player import Player
from asteroids import Asteroids
import utils
import random

class Game:
    # class const
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    ASTEROIDS_NUMBER = 10

    def __init__(self):
        self._init_pygame()  # when this class is called - init pygame method is initialized
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background = utils.load_sprite("space", False)
        self.spaceship = Player((400, 300))

        # init multiple asteroids in a list
        self.asteroid_coords = [(random.randint(0, self.SCREEN_WIDTH), random.randint(0, self.SCREEN_HEIGHT))
                                for _ in range(self.ASTEROIDS_NUMBER)]
        self.asteroids_list = [Asteroids((x, y)) for x, y in self.asteroid_coords]

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
        is_key_pressed = pygame.key.get_pressed()  # returns a list

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
        self.spaceship.move(self.screen)
        self.asteroids_list[1].move(self.screen)

        # # Check screen boundaries to keep object within screen
        # if self.spaceship.position.x < 0 or self.spaceship.position.x > self.screen.get_width():
        #     self.spaceship.velocity.x *= -1
        # elif self.spaceship.position.y < 0 or self.spaceship.position.y > self.screen.get_height():
        #     self.spaceship.velocity.y *= -1

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # fills the screen with each frame
        self.spaceship.draw(self.screen)
        self.asteroids_list[1].draw(self.screen)
        pygame.display.flip()  # updates the content of the screen
        self.clock.tick(60)  # will wait it match the desired FPS

