import sys
import pygame

# pygame settings init
pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('A Ducking Game')
font_venti = pygame.font.Font('font/Pixeltype.ttf', 200)
font_grande = pygame.font.Font('font/Pixeltype.ttf', 100)
font_tall = pygame.font.Font('font/Pixeltype.ttf', 50)
FPS = pygame.time.Clock()

game_state = 'main_menu'

main_name = font_venti.render('A Ducking Game', False, (0, 128, 0))
main_name_rect = main_name.get_rect(center=(800, 150))
main_msg = font_grande.render('Press enter to start', False, (0, 205, 0))
main_msg_rect = main_msg.get_rect(center=(800,350))
main_instruct = font_tall.render('How to play', False, (0, 205, 0))
main_instruct_rect = main_instruct.get_rect(center=(1500, 50))

background = pygame.image.load('background/full-bg.png').convert()
background = pygame.transform.scale(background, (1600, 800))

# Duck sprite
duck_idle_1 = pygame.image.load('duck/Sprites/Idle/Idle1.png').convert_alpha()
duck_idle_1_scaled = pygame.transform.scale(duck_idle_1, (200, 200))
duck_idle_2 = pygame.image.load('duck/Sprites/Idle/Idle2.png').convert_alpha()
duck_idle_2_scaled = pygame.transform.scale(duck_idle_2, (200, 200))
duck_idle = [duck_idle_1_scaled, duck_idle_2_scaled]
duck_idle_index = 0
duck = duck_idle[duck_idle_index]
duck_rect = duck.get_rect(midbottom=(80, 700))

def duck_animate():
    global duck, duck_idle_index

    duck_idle_index += 0.05
    if duck_idle_index >= len(duck_idle):
        duck_idle_index = 0
    duck = duck_idle[int(duck_idle_index)]


# game loop
while True:

    FPS.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == 'main_menu':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = 'active'
            if event.type == pygame.MOUSEBUTTONDOWN and main_instruct_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = 'instruct_menu'

    if game_state == 'main_menu':
        screen.blit(main_name, main_name_rect)
        screen.blit(main_msg, main_msg_rect)
        screen.blit(main_instruct, main_instruct_rect)
    elif game_state == 'instruct_menu':
        pass
    elif game_state == 'active':
        duck_animate()
        screen.blit(duck, duck_rect)



    pygame.display.update()
