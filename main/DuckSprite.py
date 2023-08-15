import pygame


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Idle images
        idle_1 = pygame.image.load('../resources/duck/Sprites/Idle/Idle1.png').convert_alpha()
        idle_1_scaled = pygame.transform.scale(idle_1, (200, 200))
        idle_2 = pygame.image.load('../resources/duck/Sprites/Idle/Idle2.png').convert_alpha()
        idle_2_scaled = pygame.transform.scale(idle_2, (200, 200))
        self.idle = [idle_1_scaled, idle_2_scaled]

        # Walk images
        walk_1 = pygame.image.load('../resources/duck/Sprites/Walking-Running/Walking1.png').convert_alpha()
        walk_1_scaled = pygame.transform.scale(walk_1, (200, 200))
        walk_2 = pygame.image.load('../resources/duck/Sprites/Walking-Running/Walking2.png').convert_alpha()
        walk_2_scaled = pygame.transform.scale(walk_2, (200, 200))
        self.walk = [walk_1_scaled, walk_2_scaled]

        # Jump image
        jump = pygame.image.load('../resources/duck/Sprites/Jumping/Jumping.png').convert_alpha()
        self.jumping = pygame.transform.scale(jump, (200, 200))

        # Initial state
        self.animate_state = 'Idle'
        self.animate_index = 0
        self.image = self.idle[int(self.animate_index)]
        self.rect = self.image.get_rect(midbottom=(80, 700))
        self.gravitation = 0

    def gravity(self):
        self.gravitation += 1
        self.rect.y += self.gravitation
        if self.rect.bottom >= 700:
            self.animate_state = 'Idle'
            self.rect.bottom = 700

    def user_input(self):
        input = pygame.key.get_pressed()
        # Jump
        if input[pygame.K_SPACE] and self.rect.bottom >= 700:
            self.animate_state = 'Jump'
            self.gravitation = -20
        # Move right
        if input[pygame.K_RIGHT] and self.rect.right <= 1600:
            self.rect.x += 5
            if self.rect.bottom >= 700:
                self.animate_state = 'Walk'
        # Move left
        if input[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5
            if self.rect.bottom >= 700:
                self.animate_state = 'Walk'

    def animate(self):
        if self.animate_state == 'Jump':
            self.image = self.jumping
        elif self.animate_state == 'Idle':
            self.image = self.idle[int(self.animate_index)]
            self.animate_index += 0.05
            if self.animate_index >= len(self.idle):
                self.animate_index = 0
        elif self.animate_state == 'Walk':
            self.image = self.walk[int(self.animate_index)]
            self.animate_index += 0.05
            if self.animate_index >= len(self.walk):
                self.animate_index = 0

    def update(self):
        self.animate()
        self.gravity()
        self.user_input()