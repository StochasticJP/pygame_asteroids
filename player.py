from gameobject import GameObject
import utils
from pygame.math import Vector2
from pygame.transform import rotozoom

class Player(GameObject):
    # class const
    SPACESHIP = "spaceship"
    MANEAVERABILITY = 3
    UP_DIRECTION = (0, -1)
    UP_COORDS = (0, -1)
    ACCELERATION = 0.25

    def __init__(self, position):
        super().__init__(position, utils.load_sprite(self.SPACESHIP), Vector2(0))
        self.direction = Vector2(self.UP_DIRECTION)

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEAVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(self.UP_COORDS)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
