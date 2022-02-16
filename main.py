import pygame
from objects import Birb
app = pygame.display.set_mode((640, 480))

birb = Birb(100, 100)
velocity = [0, 0]
acceralation = [0.1, 0.1]
jumpDown = False
BACKGROUND = pygame.image.load("assets/art/background.png")
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not jumpDown:
            velocity[1] -= 10
            jumpDown = True
    else:
        jumpDown = False
    app.blit(BACKGROUND, (0, 0))
    birb.y += velocity[1]
    velocity[1] += acceralation[1]
    birb.draw(app)
    pygame.display.update()
    pygame.time.delay(10)