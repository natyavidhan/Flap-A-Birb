import pygame

from dataclasses import dataclass


@dataclass
class Vector2D:
    x: float
    y: float


class Birb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._img = pygame.image.load("assets/art/birb.png").convert_alpha()
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0.1, 0.1)

    def draw(self, screen):
        screen.blit(self._img, (self.x, self.y))


class Pillar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pillarUp = pygame.image.load("assets/art/pillar.png").convert_alpha()
        self.pillarDown = pygame.transform.flip(self.pillarUp, flip_x=False, flip_y=True)
        self.scored = False

    def draw(self, screen):
        screen.blit(self.pillarUp, (self.x, self.y))
        screen.blit(
            self.pillarDown, (self.x, self.y + self.pillarUp.get_height() + 130)
        )

    def colliding(self, birb):
        return (self.x - birb._img.get_width() < birb.x < self.x + self.pillarUp.get_width()) and not \
            (self.y + self.pillarUp.get_height() <= birb.y <= self.y + self.pillarUp.get_height() + 130 - birb._img.get_height())
