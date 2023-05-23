from gameobject import GameObject
from utils import *
from pygame.math import Vector2
from pygame.transform import rotozoom
import random

class Asteroids(GameObject):
    ASTEROIDS = "asteroid"
    CONST_ROTATION = 1
    INIT_SPEED = 1
    DIRECTION_NUMBER = 5
    UP_COORDS = (0, -1)

    def __init__(self, position):
        self.init_speed = [(round(random.uniform(-1.0, 1.0), 1), round(random.uniform(-1.0, 1.0), 1))
                               for _ in range(self.DIRECTION_NUMBER)]
        self.speed = Vector2(self.init_speed[random.randint(0, len(self.init_speed)-1)])
        super().__init__(position, load_sprite(self.ASTEROIDS), get_random_velocity(1, 2))
        self.direction = Vector2(self.UP_COORDS)

    def rotate(self):
        self.direction.rotate_ip(self.CONST_ROTATION)

    def draw(self, surface):
        angle = self.direction.angle_to(self.UP_COORDS)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position
        surface.blit(rotated_surface, blit_position)

