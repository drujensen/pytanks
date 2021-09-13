import pygame as pg

from utils.load import load_image

class Wall(pg.sprite.Sprite):
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image(im) for im in ("wall1.gif", "wall2.gif", "wall3.gif")]
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=[150,150])
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
