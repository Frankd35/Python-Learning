import sys,time

import pygame


class Ship:
    def __init__(self, screen):
        """initialize the ship and its starting position"""
        self.screen = screen
        # load the ship and its rect
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        # movement flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        # set speed
        self.speed = 3

    def blit(self):
        """draw a ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, stat, ship_hit):
        if self.move_right and self.rect.right < 1200:
            self.rect.centerx += self.speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.move_up and self.rect.top > 0:
            self.rect.bottom -= self.speed
        if self.move_down and self.rect.bottom < 700:
            self.rect.bottom += self.speed
        # ship_life
        if stat.ship_life < 0:
            # print("game over")
            stat.game_play = False
        if ship_hit:
            stat.ship_life -= 1
            time.sleep(0.3)
        if stat.new_life >= 10:
            stat.new_life -= 10
            stat.ship_life += 1

