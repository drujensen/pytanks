import pygame as pg

from utils.load import load_image

class Shot(pg.sprite.Sprite):
    speed = -11
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image("shot.gif")]
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()
