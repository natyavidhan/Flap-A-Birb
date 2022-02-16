import pygame
from objects import Birb, Pillar
import random
app = pygame.display.set_mode((640, 480))

birb = Birb(100, 100)
velocity = [0, 0]
acceralation = [0.1, 0.1]
jumpDown = False
BACKGROUND = pygame.image.load("assets/art/background.png")
run = True
pillars = []
score = 0
pygame.font.init()
scoreText = pygame.font.SysFont("Arial", 30)

def createPillar():
    x = 650
    y = random.randint(-350, -150)
    pillar = Pillar(x, y)
    pillars.append(pillar)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not jumpDown:
            velocity[1] = -3
            jumpDown = True
    else:
        jumpDown = False
    app.blit(BACKGROUND, (0, 0))
    birb.y += velocity[1]
    velocity[1] += acceralation[1]
    birb.draw(app)
    #rendering pillars
    if len(pillars) < 4:
        if len(pillars) > 0:
            if 450 > pillars[-1].x + pillars[-1].pillarUp.get_width():
                createPillar()
        else:
            createPillar()
        
    for pillar in pillars:
        if pillar.x < -50:
            pillars.remove(pillar)
        if pillar.x < 75 and not pillar.scored:
            score += 1
            pillar.scored = True
        pillar.x -= 2
        pillar.draw(app)
        if pillar.colliding(birb):
            run = False
            
    text = scoreText.render(str(score), True, (0, 0, 0))
    
    textRect = text.get_rect()
    textRect.center = (320, 30)
    
    app.blit(text, textRect)
    
    
    pygame.display.update()
    pygame.time.delay(10)