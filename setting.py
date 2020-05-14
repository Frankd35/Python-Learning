import pygame


class Settings:
    """all settings for alien invasion"""

    def __init__(self):
        # screen setting
        self.screenHeight = 700
        self.screenWidth = 1200
        self.bgColor = (255, 120, 120)
        # ship speed
        self.ship_speed = 0

        self.level_2 = False
        self.level_3 = False
        self.level_4 = False

    def update(self,stat):
        if stat.kill >= 80:
            self.level_4 = True
            self.level_3 = False
        elif stat.kill >= 60:
            self.level_3 = True
            self.level_2 = False
        elif stat.kill >= 30:
            self.level_2 = True


class Button:
    def __init__(self, screen):
        self.screen = screen
        self.play = pygame.image.load('image/play.bmp')
        self.stop = pygame.image.load('image/stop.bmp')
        self.rect = self.play.get_rect()
        # self.rect.center = self.screen.get_rect().center

    def blit(self,stat):
        if not stat.game_play :
            self.screen.blit(self.play, (0,0))
        elif stat.game_play:
            self.screen.blit(self.stop, (0,0))
