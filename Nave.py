import pygame as pg
from pygame.locals import *

FPS = 60
candidatos = 0

class Nave(pg.sprite.Sprite):
    pictures = 'nave.png'
    speed = 10
    lives = 5
    #contador = 0
    def __init__(self, x=10, y=300):
        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('resources/nave/{}'.format(self.pictures)).convert_alpha()      

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h

        self.surf = self.image
        self.rect1 = self.surf.get_rect(x=700, y=300)

    def rot_center(self,image, angle):
        orig_rect = image.get_rect()
        rot_image = pg.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def go_up(self):
        self.rect.y = max(0, self.rect.y - self.speed)  
        if self.y <= 0:
            self.rect.y = 0

    def go_down(self):
        self.rect.y = min(self.rect.y + self.speed, 600-self.w)     
        if self.y >= 600:
            self.rect.y = 600 

    def test_collide(self, group):
        self.candidatos = pg.sprite.spritecollide(self, group, True)

    
  