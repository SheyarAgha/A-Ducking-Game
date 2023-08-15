import pygame


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Duck idle images
        idle_1 = pygame.image.load('../resources/duck/Sprites/Idle/Idle1.png').convert_alpha()
        idle_1_scaled = pygame.transform.scale(idle_1, (200, 200))
        idle_2 = pygame.image.load('../resources/duck/Sprites/Idle/Idle2.png').convert_alpha()
        idle_2_scaled = pygame.transform.scale(idle_2, (200, 200))
        self.idle = [idle_1_scaled, idle_2_scaled]
        self.idle_index = 0
        self.image = self.idle[int(self.idle_index)]
        self.rect = self.image.get_rect(midbottom=(80, 700))

    def animate(self):
        self.idle_index += 0.05
        if self.idle_index >= len(self.idle):
            self.idle_index = 0
        self.image = self.idle[int(self.idle_index)]

    def update(self):
        self.animate()