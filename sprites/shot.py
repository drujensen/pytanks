import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image

class Shot(pg.sprite.Sprite):
    speed = -11
    rotation = 90
    images = []
    x = 0
    y = 0

    def __init__(self, pos, rotation):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image(im) for im in ("shot-0.png", "shot-1.png", "shot-2.png", "shot-3.png", "shot-4.png", "shot-5.png", "shot-6.png", "shot-7.png")]
        self.image = self.images[2]
        self.rect = self.image.get_rect()
        self.rotation = rotation
        self.rect.center = pos.center

    def update(self):
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
        self.rect.move_ip(-x * self.speed, -y * self.speed)
        if not SCREENRECT.contains(self.rect):
            self.kill()
