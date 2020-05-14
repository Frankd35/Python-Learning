import sys

import pygame,random
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship, *groups):
        """initialize bullet"""
        super().__init__(*groups)
        self.screen = screen
        # color
        self.gray = pygame.image.load('image/graybullet.bmp')
        self.white = pygame.image.load('image/whitebullet.bmp')
        self.blue = pygame.image.load('image/bluebullet.bmp')
        self.purple = pygame.image.load('image/purplebullet.bmp')
        self.yellow = pygame.image.load('image/yellowbullet.bmp')
        self.red = pygame.image.load('image/redbullet.bmp')
        self.colorList = [self.gray, self.purple, self.white, self.blue, self.yellow, self.red]
        # self.color_change = False
        self.color = random.choice(self.colorList)
        # set rect and position for bullet
        self.rect = self.purple.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # speed
        self.speed = 2

    def update(self, ship, bullets):
        """move up to top"""
        # move bullet
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            bullets.remove(self)

    def blit(self):
        self.screen.blit(self.color, self.rect)



