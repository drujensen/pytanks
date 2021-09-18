import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image

class Shot(pg.sprite.Sprite):
    speed = -11
    rotation = 0
    images = []
    x = 0
    y = 0

    def __init__(self, pos, rotation):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image("shot.gif")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rotation = rotation
        self.rect.center = pos.center

    def update(self):
        if self.rotation >= 0:
            x = 0
            y = -1
        if self.rotation >= 45:
            x = 1
            y = -1
        if self.rotation >= 90:
            x = 1
            y = 0
        if self.rotation >= 135:
            x = 1
            y = 1
        if self.rotation >= 180:
            x = 0
            y = 1
        if self.rotation >= 225:
            x = -1
            y = 1
        if self.rotation >= 270:
            x = -1
            y = 0
        if self.rotation >= 315:
            x = -1
            y = -1
        self.rect.move_ip(-x * self.speed, -y * self.speed)
        if not SCREENRECT.contains(self.rect):
            self.kill()
