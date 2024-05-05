import pygame
import sys
import time
from btn import ImageButton

clock = pygame.time.Clock()
WDTH = 960
HGHT = 600
pygame.init()
pygame.mixer.music.load('OMFG_-_I_Love_You_64374777.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.13)

screen = pygame.display.set_mode((WDTH, HGHT))
menu_screen = pygame.display.set_mode((WDTH,HGHT))
menu_background = pygame.image.load("img/menub.jpg")
menu_background = pygame.transform.scale(menu_background, (WDTH,HGHT))
pygame.display.set_caption("Gravityscapes")
icon = pygame.image.load("img/Gravity.jpg")
pygame.display.set_icon(icon)
background = pygame.image.load("img/brickwall.png")
background = pygame.transform.scale(background, (WDTH, HGHT))
obstacle = pygame.image.load("img/walls.png")
floor = pygame.transform.scale(obstacle,(WDTH,150))
roof = pygame.transform.scale(obstacle,(WDTH,50))
obstacle1 = pygame.transform.scale(obstacle,(50,HGHT/2))
obstacle2 = pygame.transform.scale(obstacle,(50,HGHT/2))
door = pygame.image.load("img/door.png")
door = pygame.transform.scale(door,(50,80))

def main_menu():
    start_button = ImageButton(WDTH/2-(252/2), 150, 252, 74, "Новая игра", "img/Gravity.jpg", "img/left/left1.png")
    exit_button = ImageButton(WDTH/2-(252/2), 250, 252, 74, "Выход", "img/Gravity.jpg", "img/left/left1.png")

    running = True
    while running:
        menu_screen.fill((0,0,0))
        menu_screen.blit(menu_background, (0,0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU TEST", True, (255,255,255))
        text_rect = text_surface.get_rect(center=(WDTH/2, 100))
        menu_screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                game()
            elif event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, exit_button]:
                btn.handle_event(event)
        
        for btn in [start_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(menu_screen)

        pygame.display.flip()


def game():
    player_still = pygame.image.load("img/still.png")
    font = pygame.font.Font(None, 102)
    text_surface = font.render('Победа!', True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WDTH/2, HGHT/2))


    walk_left = [
        pygame.image.load("img/left/left1.png"),
        pygame.image.load("img/left/left2.png"),
        pygame.image.load("img/left/left3.png"),
        pygame.image.load("img/left/left4.png"),
        pygame.image.load("img/left/left5.png"),
        pygame.image.load("img/left/left6.png"),
        pygame.image.load("img/left/left7.png"),
        pygame.image.load("img/left/left8.png"),
        pygame.image.load("img/left/left9.png")
    ]

    walk_right = [
        pygame.image.load("img/right/right1.png"),
        pygame.image.load("img/right/right2.png"),
        pygame.image.load("img/right/right3.png"),
        pygame.image.load("img/right/right4.png"),
        pygame.image.load("img/right/right5.png"),
        pygame.image.load("img/right/right6.png"),
        pygame.image.load("img/right/right7.png"),
        pygame.image.load("img/right/right8.png"),
        pygame.image.load("img/right/right9.png")
    ]

    player_anim_count = 0


    bg_x = 0

    player_speed = 5
    player_x = 150
    player_y = 450
    jump_count = 13

    is_jump = False
    running = True
    while running:
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + WDTH, 0))

        screen.blit(floor,(0,500))
        screen.blit(roof,(0,0))
        screen.blit(obstacle1,(300,0))
        screen.blit(obstacle2,(500,HGHT/2))
        screen.blit(obstacle1,(700,0))
        screen.blit(door,(800,50))
        screen.blit(text_surface,text_rect)

        if 700 < player_x < 900 and 0 < player_y < 120:
            screen.blit(text_surface,text_rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_still, (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 850:
            player_x += player_speed
        
        if not is_jump and keys[pygame.K_SPACE]:
                is_jump = True
        elif is_jump and keys[pygame.K_UP]:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 13
        elif is_jump and keys[pygame.K_DOWN]:
            if jump_count > 0:
                player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 13

        if player_anim_count == 8:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        if keys[pygame.K_ESCAPE]:
            main_menu()
        
        clock.tick(10)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()