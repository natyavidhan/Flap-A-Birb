import pygame
from objects import Birb, Pillar
import random

app = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.font.init()

# *** global game state ***
birb = Birb(100, 100)
keys_prev = {}
pillars = []
score = 0


class Assets:
    score_text = pygame.font.SysFont("Arial", 30)
    background = pygame.image.load("assets/art/background.png")


createPillar = lambda: Pillar(650, random.randint(-350, -150))


def draw_score(score: int):
    text = Assets.score_text.render(str(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (320, 30)
    app.blit(text, textRect)


def run_update():
    global score, keys_prev

    # *** handle user input ***
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not keys_prev[pygame.K_UP]:
        birb.velocity.y = -3
    keys_prev = keys

    # *** handle+draw birb ***
    app.blit(Assets.background, (0, 0))
    birb.y += birb.velocity.y
    birb.velocity.y += birb.acceleration.y
    birb.draw(app)
    if not 0 <= birb.y <= 480:
        return

    # *** handle+draw pillars ***
    if max((pillar.x for pillar in pillars), default=0) < 390:
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
            return

    draw_score(score)
    return True


while run_update():
    pygame.display.update()
    clock.tick(60)  # fps
