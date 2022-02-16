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
        self.pillarUp = pygame.image.load(
            "assets/art/pillar.png").convert_alpha()
        self.pillarDown = pygame.image.load(
            "assets/art/pillar.png").convert_alpha()
        self.pillarDown = pygame.transform.flip(self.pillarDown, False, True)

    def draw(self, screen):
        screen.blit(self.pillarUp, (self.x, self.y))
        screen.blit(self.pillarDown, (self.x, self.y +
                                      self.pillarUp.get_height()+130))

    def colliding(self, birb):
        if birb.x + birb.birb.get_width() > self.x and birb.x < self.x + self.pillarUp.get_width() or birb.x + birb.birb.get_width() > self.x and birb.x < self.x + self.pillarDown.get_width():
            if birb.y + birb.birb.get_height() > self.y and birb.y < self.y + self.pillarUp.get_height() or birb.y + birb.birb.get_height() > self.y + self.pillarUp.get_height()+130 and birb.y < self.y + self.pillarUp.get_height()+130 + self.pillarDown.get_height():
                return True
        return False
