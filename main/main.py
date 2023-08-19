import sys
import zmq
import pygame
import json
from DuckSprite import Duck
from FoxSprite import Fox

# pygame settings init
pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('A Ducking Game')
font_venti = pygame.font.Font('../resources/font/Pixeltype.ttf', 200)
font_grande_er = pygame.font.Font('../resources/font/Pixeltype.ttf', 150)
font_grande = pygame.font.Font('../resources/font/Pixeltype.ttf', 100)
font_tall = pygame.font.Font('../resources/font/Pixeltype.ttf', 50)
FPS = pygame.time.Clock()
time = 0
current_score = 0
current_player = 'Player1'
leaderboard = {}

game_state = 'main_menu'

main_name = font_venti.render('A Ducking Game', False, (0, 128, 0))
main_name_rect = main_name.get_rect(center=(800, 150))
main_msg = font_grande.render('Press enter to start', False, (0, 205, 0))
main_msg_rect = main_msg.get_rect(center=(800,350))
main_instruct = font_tall.render('How to play', False, (0, 205, 0))
main_instruct_rect = main_instruct.get_rect(center=(1500, 50))
main_leaderboard = font_tall.render('Leaderboard', False, (0, 205, 0))
main_leaderboard_rect = main_leaderboard.get_rect(center=(120, 50))

leaderboard_menu = font_grande_er.render('Leaderboard', False, (0, 205, 0))
leaderboard_menu_rect = leaderboard_menu.get_rect(center=(800, 150))
leaderboard_back = font_tall.render('Main Menu', False, (0, 205, 0))
leaderboard_back_rect = leaderboard_back.get_rect(center=(120, 50))

background = pygame.image.load('../resources/background/full-bg.png').convert()
background = pygame.transform.scale(background, (1600, 800))

player = pygame.sprite.GroupSingle()
enemy = pygame.sprite.Group()

# Initialize connection to microservice
context = zmq.Context()
print("Connecting to leaderboard microservice...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8888")
print("Connected!")


def get_leaderboard():
    # Send request
    print("Sending request for current leaderboard")
    socket.send(b"get_leaderboard")
    # Receive request
    data = socket.recv()
    data = data.decode('utf-8').replace("\'", "\"")
    data = json.loads(data)
    return data

def update_leaderboard(new_data):
    # Send request
    print("Sending request to update leaderboard")
    socket.send(b"add_to_leaderboard")
    response = socket.recv()
    if response == b"ready":
        print("Microservice ready!")
        print("Updating leaderboard")
        socket.send(str(new_data).encode())
    response = socket.recv()
    if response == b"added":
        print("Successfully updated leaderboard")
    else:
        print("Failed to update")


def collision_state():
    if pygame.sprite.spritecollide(player.sprite, enemy, False):
        enemy.empty()
        return 'lose'
    else:
        return 'active'


def display_score():
    current_score = int(pygame.time.get_ticks() / 1000) - time
    score = font_grande.render(f'{current_score}', False, (64, 64, 64))
    score_rect = score.get_rect(center=(800, 100))
    screen.blit(score, score_rect)
    return current_score


def initiate_sprites():
    player.add(Duck())
    enemy.add(Fox())

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
                initiate_sprites()
                time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.MOUSEBUTTONDOWN and main_instruct_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = 'instruct_menu'
            if event.type == pygame.MOUSEBUTTONDOWN and main_leaderboard_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = 'leaderboard'
                leaderboard = get_leaderboard()
        elif game_state == 'leaderboard':
            if event.type == pygame.MOUSEBUTTONDOWN and leaderboard_back_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = 'main_menu'
        elif game_state == 'lose':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = 'main_menu'
                update_leaderboard({"name": current_player, "score": current_score})

    if game_state == 'main_menu':
        screen.blit(main_name, main_name_rect)
        screen.blit(main_msg, main_msg_rect)
        screen.blit(main_instruct, main_instruct_rect)
        screen.blit(main_leaderboard, main_leaderboard_rect)
    elif game_state == 'instruct_menu':
        pass
    elif game_state == 'leaderboard':
        screen.blit(leaderboard_menu, leaderboard_menu_rect)
        screen.blit(leaderboard_back, leaderboard_back_rect)
        name = leaderboard["name"]
        highscore = font_grande.render(f'{leaderboard["name"]}     {leaderboard["score"]}', False, (111, 196, 169))
        highscore_rect = highscore.get_rect(center=(800, 250))
        screen.blit(highscore, highscore_rect)
    elif game_state == 'active':
        current_score = display_score()
        player.draw(screen)
        player.update()
        enemy.draw(screen)
        enemy.update()
        game_state = collision_state()
    elif game_state == 'lose':
        screen.fill((94, 129, 162))
        score_message = font_grande.render(f'Your score: {current_score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(800, 250))
        screen.blit(score_message, score_message_rect)
        return_message = font_grande.render('Press enter to return to menu', False, (111, 196, 169))
        return_message_rect = return_message.get_rect(center=(800, 350))
        screen.blit(return_message, return_message_rect)


    pygame.display.update()
