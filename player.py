from gameobject import GameObject
import utils
from pygame.math import Vector2
from pygame.transform import rotozoom
from player_weapons import Weapons


class Player(GameObject):
    # class const
    SPACESHIP = "spaceship"
    MANEAVERABILITY = 3  # how fast the spaceship rotates
    UP_COORDS = (0, -1)
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback):
        super().__init__(position, utils.load_sprite(self.SPACESHIP), Vector2(0))
        self.direction = Vector2(GameObject.UP_DIRECTION)
        self.create_bullet_callback = create_bullet_callback

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEAVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(self.UP_COORDS)  # checks the difference between up and current direction
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)  # put on screen using blit_pos

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity  # relative speed
        bullet = Weapons(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)
