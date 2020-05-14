import pygame


class Board:
    """ create a dynamic score board"""

    def __init__(self, screen, stat):
        """set statistic board"""
        self.score = stat.score
        self.screen = screen
        self.life = stat.ship_life
        self.text_color = (255, 255, 0)
        self.board_color = (255, 120, 120)
        self.font = pygame.font.SysFont('arial', 44)
        # score board
        self.score_image = self.font.render(str(self.score), True, self.text_color, self.board_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.width *= 5
        self.score_rect.right = 1200
        self.score_rect.top = self.screen.get_rect().top
        # life board
        self.life_image = self.font.render("left life : "+str(self.life), True, self.text_color, self.board_color)
        self.life_rect = self.life_image.get_rect()
        self.life_rect.centerx = self.screen.get_rect().centerx
        self.life_rect.top = self.screen.get_rect().top

    def updata(self, stat):
        """Turn the recent score, left lives into a rendered image."""
        self.score = stat.score
        self.life = stat.ship_life
        self.score_image = self.font.render(str(self.score), True, self.text_color, self.board_color)
        self.life_image = self.font.render("rest life : "+str(self.life), True, self.text_color, self.board_color)

    def blit(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.life_image,self.life_rect)

    def welcome_board(self):
        self.screen.blit(pygame.image.load('image/welcome.bmp'), (0,0))
