import pygame
app = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    app.fill((0, 0, 0))
    pygame.display.update()
    pygame.time.delay(10)