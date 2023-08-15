import pygame


class Fox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Run images
        run_1 = pygame.image.load('../resources/Fox/run/foxrun1.png').convert_alpha()
        run_1_scaled = pygame.transform.scale(run_1, (100, 100))
        run_2 = pygame.image.load('../resources/Fox/run/foxrun2.png').convert_alpha()
        run_2_scaled = pygame.transform.scale(run_2, (100, 100))
        run_3 = pygame.image.load('../resources/Fox/run/foxrun3.png').convert_alpha()
        run_3_scaled = pygame.transform.scale(run_3, (100, 100))
        run_4 = pygame.image.load('../resources/Fox/run/foxrun4.png').convert_alpha()
        run_4_scaled = pygame.transform.scale(run_4, (100, 100))
        run_5 = pygame.image.load('../resources/Fox/run/foxrun5.png').convert_alpha()
        run_5_scaled = pygame.transform.scale(run_5, (100, 100))
        run_6 = pygame.image.load('../resources/Fox/run/foxrun6.png').convert_alpha()
        run_6_scaled = pygame.transform.scale(run_6, (100, 100))
        run_7 = pygame.image.load('../resources/Fox/run/foxrun7.png').convert_alpha()
        run_7_scaled = pygame.transform.scale(run_7, (100, 100))
        run_8 = pygame.image.load('../resources/Fox/run/foxrun8.png').convert_alpha()
        run_8_scaled = pygame.transform.scale(run_8, (100, 100))
        self.run = [run_1_scaled, run_2_scaled, run_3_scaled, run_4_scaled, run_5_scaled,
                     run_6_scaled, run_7_scaled, run_8_scaled]

        # Initial State
        self.animate_index = 0
        self.image = self.run[int(self.animate_index)]
        self.rect = self.image.get_rect(midbottom=(1700, 700))
        self.run_speed = 5

    def animate(self):
        self.animate_index += 0.3
        if self.animate_index >= len(self.run):
            self.animate_index = 0
        self.image = self.run[int(self.animate_index)]

        self.rect.x -= self.run_speed
        if self.rect.right < 0:
            self.rect.left = 1700

    def update(self):
        self.animate()
