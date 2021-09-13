import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image
class Tank(pg.sprite.Sprite):
    speed = 10
    bounce = 24
    gun_offset = -11

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        img = load_image("tank.gif")
        self.images = [img, pg.transform.flip(img, 1, 0)]

        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top