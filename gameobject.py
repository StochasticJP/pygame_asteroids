from utils import *
from pygame.math import Vector2


class GameObject:
    UP_DIRECTION = Vector2(0, -1)  # unit vectors

    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)  # blit requires top-left corner
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)

        # collision logic
        if distance < self.radius + other_obj.radius:
            return distance