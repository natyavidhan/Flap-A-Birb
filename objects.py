import pygame

class Birb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.birb = pygame.image.load("assets/art/birb.png").convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.birb, (self.x, self.y))

class Pillar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pillar = pygame.image.load("assets/art/pillar.png").convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.pillar, (self.x, self.y))