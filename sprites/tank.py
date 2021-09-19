import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image
from random import randint
class Tank(pg.sprite.Sprite):
    speed = 5
    rotation = 0 # 0 to 359.  0 is north, 90 is east, 180 is south, 270 is west
    direction = 0 # -1 to 1.  -1 is backward, 0 is not moving, 1 is forward
    color = (255,0,0)
    size = (20, 20)
    images = []

    def __init__(self, startx):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        starty = randint(0,SCREENRECT.height - self.rect.height)
        self.rect.center=[startx, starty]
        self.reloading = 0
        self.origtop = self.rect.top

    def move(self, direction, rotation):
        if rotation:
            self.rotation += rotation * self.speed
            if self.rotation > 359: self.rotation = 0
            if self.rotation < 0: self.rotation = 359
        if direction:
            self.direction = direction
        else:
            self.direction = 0
        
        if self.rotation >= 0:
            self.image = self.images[0]
            self.gunpos = self.rect.midtop
            x = 0
            y = -1
        if self.rotation >= 45:
            self.image = self.images[1]
            self.gunpos = self.rect.topright
            x = 1
            y = -1
        if self.rotation >= 90:
            self.image = self.images[2]
            self.gunpos = self.rect.midright
            x = 1
            y = 0
        if self.rotation >= 135:
            self.image = self.images[3]
            self.gunpos = self.rect.bottomright
            x = 1
            y = 1
        if self.rotation >= 180:
            self.image = self.images[4]
            self.gunpos = self.rect.midbottom
            x = 0
            y = 1
        if self.rotation >= 225:
            self.image = self.images[5]
            self.gunpos = self.rect.bottomleft
            x = -1
            y = 1
        if self.rotation >= 270:
            self.image = self.images[6]
            self.gunpos = self.rect.midleft
            x = -1
            y = 0
        if self.rotation >= 315:
            self.image = self.images[7]
            self.gunpos = self.rect.topleft
            x = -1
            y = -1
        self.rect.width = self.image.get_rect().width
        self.rect.height = self.image.get_rect().height
        self.rect.move_ip(x * self.direction * self.speed, y * self.direction * self.speed)
        self.rect = self.rect.clamp(SCREENRECT)
