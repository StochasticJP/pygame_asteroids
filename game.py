import pygame
from gameobject import GameObject
from player import Player
from asteroids import Asteroids
from player_weapons import Weapons
import utils
import random
import time

class Game:
    # class const
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    ASTEROIDS_NUMBER = 5
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        self._init_pygame()  # when this class is called - init pygame method is initialized
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background = utils.load_sprite("space", False)
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.asteroids = []
        self.bullets = []
        self.spaceship = Player((400, 300), self.bullets.append)

        # init multiple asteroids in a list
        # self.asteroid_coords = [(random.randint(0, self.SCREEN_WIDTH), random.randint(0, self.SCREEN_HEIGHT))
        #                        for _ in range(self.ASTEROIDS_NUMBER)]

        # self.asteroid_coords = [(utils.get_random_position(self.screen)) for _ in range(self.ASTEROIDS_NUMBER)]
        # self.asteroids_list = [Asteroids((x, y)) for x, y in self.asteroid_coords]

        for _ in range(self.ASTEROIDS_NUMBER):
            while True:
                position = utils.get_random_position(self.screen)
                if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
                    break

            self.asteroids.append(Asteroids(position, self.asteroids.append))


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

        if self.spaceship:  # check if spaceship exists
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
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None  # removes the spaceship
                    self.message = "You Lost!"
                    break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if bullet.collides_with(asteroid):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    asteroid.split()
                    break

        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = "You Won!"

        # self.spaceship.move(self.screen)
        #
        # for asteroids in self.asteroids_list:
        #     asteroids.move(self.screen)



        # # Check screen boundaries to keep object within screen
        # if self.spaceship.position.x < 0 or self.spaceship.position.x > self.screen.get_width():
        #     self.spaceship.velocity.x *= -1
        # elif self.spaceship.position.y < 0 or self.spaceship.position.y > self.screen.get_height():
        #     self.spaceship.velocity.y *= -1

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # fills the screen with each frame

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message:
            utils.print_text(self.screen, self.message, self.font)

        # self.spaceship.draw(self.screen)
        # # asteroid drawing
        # for asteroids in self.asteroids_list:
        #     asteroids.draw(self.screen)
        #     asteroids.rotate()

        pygame.display.flip()  # updates the content of the screen
        self.clock.tick(60)  # will wait it match the desired FPS


    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects  # return a list with Objects

