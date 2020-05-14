import time
import pygame

from pygame.sprite import Group
from scoreboard import Board
from setting import Settings,Button
from ship import Ship
from game_stats import GameStat
import game_function as gf


def run_game():
    """initialize game and set a screen object, begin main loop"""
    pygame.init()
    # set bgm
    pygame.mixer.music.load('./music/bgm.mp3')
    pygame.mixer.music.play(-1,0.0)
    # set screen obj
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth,settings.screenHeight))
    pygame.display.set_caption('alien invasion')
    # set statistic, play button, scoreboard
    stat = GameStat()
    board = Board(screen,stat)
    play_button = Button(screen)
    # set ship obj
    ship = Ship(screen)
    # set bullets obj
    bullets = Group()
    # set alien obj
    aliens = Group()  # Alien(screen, settings, ship, bullets)
    gf.create_fleet(screen,settings,ship,bullets,aliens)
    # welcome
    board.welcome_board()
    pygame.display.flip()
    time.sleep(7)   # time to show welcome board
    # main loop
    while True:
        if stat.game_play:
            aliens_hit_bullet = pygame.sprite.groupcollide(bullets, aliens, True, True)
            ship_hit = pygame.sprite.spritecollide(ship, aliens, True)
            gf.event_checking(screen, ship, settings, bullets, aliens, stat, play_button)
            gf.stat_updating(settings, stat, board, aliens_hit_bullet, ship_hit)
            ship.update(stat, ship_hit)
            aliens.update(ship,bullets)
            bullets.update(ship,bullets)
            gf.new_fleet(screen, settings, ship, bullets, aliens, stat, play_button, board)   # if needed
            gf.screen_updating(screen, settings, ship, bullets, aliens, stat, play_button, board)
        elif not stat.game_play:
            gf.new_game(screen, ship, settings, bullets, aliens, stat, play_button, board)
            gf.event_checking(screen, settings, ship, bullets, aliens, stat, play_button)


run_game()
