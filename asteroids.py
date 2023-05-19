from gameobject import GameObject
from utils import *
from pygame.math import Vector2
from pygame.transform import rotozoom

class Asteroids(GameObject):
    ASTEROIDS = "asteroid"
    CONST_ROTATION = 1
    UP_COORDS = (0, -1)
    INIT_SPEED = 1

    def __init__(self, position):
        super().__init__(position, load_sprite(self.ASTEROIDS), Vector2(self.INIT_SPEED))
        self.direction = Vector2(self.UP_COORDS)


    def rotate(self):
        self.direction.rotate_ip(self.CONST_ROTATION)

    def draw(self, surface):
        angle = self.direction.angle_to(self.UP_COORDS)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)