from gameobject import GameObject
import utils
from pygame.math import Vector2


class Weapons(GameObject):
    WEAPON = 'bullet'

    def __init__(self, position, velocity):
        super().__init__(position, utils.load_sprite(self.WEAPON), velocity)
        self.position = position
        self.velocity = velocity

    def move(self, surface):
        self.position = self.position + self.velocity
