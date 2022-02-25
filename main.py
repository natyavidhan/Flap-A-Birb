import pygame
from objects import Birb, Pillar
import random
app = pygame.display.set_mode((640, 480))

birb = Birb(100, 100)
jumpDown = False
BACKGROUND = pygame.image.load("assets/art/background.png")
run = True
pillars = []
score = 0
pygame.font.init()
scoreText = pygame.font.SysFont("Arial", 30)

createPillar = lambda: Pillar(650, random.randint(-350, -150))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not jumpDown:
            birb.velocity.y = -3
            jumpDown = True
    else:
        jumpDown = False
    app.blit(BACKGROUND, (0, 0))
    birb.y += birb.velocity.y
    birb.velocity.y += birb.acceleration.y
    birb.draw(app)
    #rendering pillars
    if len(pillars) < 4:
        if len(pillars) > 0:
            if 450 > pillars[-1].x + pillars[-1].pillarUp.get_width():
                pillars.append(createPillar())
        else:
            pillars.append(createPillar())
    for pillar in pillars.copy():
        if pillar.x < -50:
            pillars.remove(pillar)
        if pillar.x < 75 and not pillar.scored:
            score += 1
            pillar.scored = True
        pillar.x -= 2
        pillar.draw(app)
        if pillar.colliding(birb):
            run = False
    if birb.y > 480 or birb.y < 0:
        run = False
            
    text = scoreText.render(str(score), True, (0, 0, 0))
    
    textRect = text.get_rect()
    textRect.center = (320, 30)
    
    app.blit(text, textRect)
    
    
    pygame.display.update()
    pygame.time.delay(10)
