import pygame

class Birb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.birb = pygame.image.load("assets/art/birb.png").convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.birb, (self.x, self.y))