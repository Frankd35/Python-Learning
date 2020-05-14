import pygame,random

from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
        # number in row

    def __init__(self, screen, settings, ship, bullet, *groups):
        """initialize alien"""
        r_image, l_image = './image/pigleft.jpg', './image/pigright.jpg'
        super().__init__(*groups)
        self.screen = screen
        self.settings = settings
        # level settings
        if settings.level_2 :
            l_image = './image/pigleft.jpg'
            r_image = './image/pigright.jpg'
            # self.speed = 3
        elif settings.level_3:
            l_image = './image/ykx.jpg'
            r_image = './image/ykx.jpg'
        elif settings.level_4:
            l_image = './image/ykx.jpg'
            r_image = './image/ykx.jpg'
        # image
        self.l_image = pygame.image.load(l_image)
        self.r_image = pygame.image.load(r_image)
        self.rect = self.l_image.get_rect()
        self.rect.centerx += self.rect.width
        self.image = self.l_image
        # movement
        self.y = self.rect.y
        self.up_and_down = random.choice([-1,-2,-3])
        self.speed = 1
        if settings.level_3:
            self.speed = 0
        elif settings.level_4:
            self.speed = 1




    def update(self, *args):
        # move direction
        if self.rect.right >= 1200:
            self.speed *= -1
        elif self.rect.left <= 0:
            self.speed *= -1
        if self.rect.top <= 0:
            self.up_and_down *= -1
        elif self.rect.bottom >= 700:
            self.up_and_down *= -1
        # image direction
        if self.speed > 0:
            self.image = self.l_image
        elif self.speed < 0:
            self.image = self.r_image
        self.rect.x += self.speed
        self.y += self.up_and_down
        self.rect.y = self.y

    def alienNo(self):
        availableSpace = self.settings.screenWidth - 2*self.rect.width
        alienNO = availableSpace / (2*self.rect.width)
        return int(alienNO)

    def blit(self):
        self.screen.blit(self.image,self.rect)

