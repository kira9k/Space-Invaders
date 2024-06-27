import pygame
from pygame.sprite import Sprite

class Health(Sprite):

    def __init__(self, screen):
        """количество жизней"""
        super(Health, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/heart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
