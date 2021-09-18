import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image
class Tank(pg.sprite.Sprite):
    speed = 5
    rotation = 90 # 0 to 359.  0 is north, 90 is east, 180 is south, 270 is west
    direction = 0 # -1 to 1.  -1 is backward, 0 is not moving, 1 is forward
    color = (255,0,0)
    size = (20, 20)
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image(im) for im in ("blue-tank-0.png", "blue-tank-1.png", "blue-tank-2.png", "blue-tank-3.png", "blue-tank-4.png", "blue-tank-5.png", "blue-tank-6.png", "blue-tank-7.png" )]
        self.image = self.images[2]
        self.rect = self.image.get_rect()
        self.rect.center=[0, (SCREENRECT.height / 2) - self.rect.height]
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
            x = 0
            y = -1
        if self.rotation >= 45:
            self.image = self.images[1]
            x = 1
            y = -1
        if self.rotation >= 90:
            self.image = self.images[2]
            x = 1
            y = 0
        if self.rotation >= 135:
            self.image = self.images[3]
            x = 1
            y = 1
        if self.rotation >= 180:
            self.image = self.images[4]
            x = 0
            y = 1
        if self.rotation >= 225:
            self.image = self.images[5]
            x = -1
            y = 1
        if self.rotation >= 270:
            self.image = self.images[6]
            x = -1
            y = 0
        if self.rotation >= 315:
            self.image = self.images[7]
            x = -1
            y = -1

        self.rect.move_ip(x * self.direction * self.speed, y * self.direction * self.speed)
        self.rect = self.rect.clamp(SCREENRECT)

    def gunpos(self):
        return self.rect