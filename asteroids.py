from gameobject import GameObject
from utils import *
from pygame.math import Vector2
from pygame.transform import rotozoom
import random


class Asteroids(GameObject):
    ASTEROIDS = "asteroid"
    ROT_SPEED = -1

    def __init__(self, position, create_asteroid_callback, size=3):
        self.size = size
        self.create_asteroid_callback = create_asteroid_callback
        self.angle = 0

        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite(self.ASTEROIDS), 0, scale)

        super().__init__(position, sprite, get_random_velocity(1, 2))

    # func that splits the asteroid when hit
    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroids(self.position, self.create_asteroid_callback, self.size - 1)
                self.create_asteroid_callback(asteroid)

    # override inheritance draw for rotational movement
    def draw(self, surface):
        self.angle += self.ROT_SPEED
        rotated_surface = rotozoom(self.sprite, self.angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)