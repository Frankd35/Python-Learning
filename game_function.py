import sys,time

import pygame
from bullet import Bullet
from alien import Alien


def event_checking(screen, ship, settings, bullets, aliens, stat, play_button):
    # detect and response to mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # a key for exit
            if event.key == pygame.K_q:
                sys.exit()
            # cheat
            if event.key == pygame.K_v:
                stat.kill += 20
            # shooting
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound('./music/shoot.wav').play()
                # set number limit
                if len(bullets) < 5:
                    bullet = Bullet(screen, ship)
                    bullets.add(bullet)
            # movement flag
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ship.move_left = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                ship.move_up = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                ship.move_down = True
        elif event.type == pygame.KEYUP:
            # movement flag
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ship.move_left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                ship.move_up = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                ship.move_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # play game button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stat, play_button, mouse_x, mouse_y)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x, mouse_y


def screen_updating(screen, settings, ship, bullets, aliens, stat, play_button, board):
    # set background color
    screen.fill(settings.bgColor)
    # # screen_bg = pygame.image.load("image/pigright.jpg")
    # # screen.blit(screen_bg,(0,0))
    # refresh screen
    ship.blit()
    play_button.blit(stat)
    for alien in aliens:
        alien.blit()
    for bullet in bullets:
        bullet.blit()
    board.blit()
    pygame.display.flip()


def create_fleet(screen, settings, ship, bullets, aliens):
    alien = Alien(screen, settings, ship, bullets)
    for line in range(2):
        for i in range(alien.alienNo()):
            alien = Alien(screen, settings, ship, bullets)
            alien.rect.x = 20 + alien.rect.x + 2 * i * alien.rect.width
            alien.y = alien.rect.y = alien.rect.y + 1.2 * line * alien.rect.height
            aliens.add(alien)


def new_fleet(screen, settings, ship, bullets, aliens, stat, play_button, board):
    if len(aliens) == 0 :
        bullets.empty()
        create_fleet(screen,settings,ship,bullets,aliens)
        screen_updating(screen, settings, ship, bullets, aliens, stat, play_button, board)
        time.sleep(1)


def new_game(screen, ship, settings, bullets, aliens, stat, play_button, board):
    bullets.empty()
    aliens.empty()
    ship.rect.centerx = ship.screenRect.centerx
    ship.rect.bottom = ship.screenRect.bottom
    stat.reset()
    screen_updating(screen, settings, ship, bullets, aliens, stat, play_button, board)


def check_play_button(stat, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stat.game_play = not stat.game_play


def stat_updating(settings, stat, board, aliens_hit_bullet,ship_hit):
    settings.update(stat)
    if aliens_hit_bullet:
        pygame.mixer.Sound('./music/hit.wav').play()
        stat.kill += 1
        stat.new_life += 1
        stat.score += stat.alien_value
    if ship_hit:
        pygame.mixer.Sound('./music/die.wav').play()
        stat.kill += 1
        stat.new_life += 1
        stat.score -= 1
    board.updata(stat)