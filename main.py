import sys
import pygame

# pygame settings init
pygame.init()
window = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('A Ducking Game')
FPS = pygame.time.Clock()

bg = pygame.image.load('background/full-bg.png').convert()
bg = pygame.transform.scale(bg, (1600, 800))

# game loop
while True:

    FPS.tick(60)
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
