import pygame as pg

from config.settings import SCREENRECT
from utils.load import load_image
from random import randint
class Wall(pg.sprite.Sprite):
    images = []
    buffer = 100

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.images = [load_image("bricks.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        x = randint(self.buffer, SCREENRECT.width - self.rect.width - self.buffer)
        y = randint(0,SCREENRECT.height - self.rect.height)
        self.rect.center = [x,y]
        self.origtop = self.rect.top

