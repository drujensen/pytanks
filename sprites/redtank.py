import pygame as pg

from sprites.tank import Tank
from utils.load import load_image
from config.settings import SCREENRECT

class RedTank(Tank):
    def __init__(self):
        self.images = [load_image(im) for im in ("red-tank-0.png", "red-tank-1.png", "red-tank-2.png", "red-tank-3.png", "red-tank-4.png", "red-tank-5.png", "red-tank-6.png", "red-tank-7.png" )]
        self.rotation = 270
        self.image = self.images[6]
        Tank.__init__(self, SCREENRECT.width)
        self.gunpos = self.rect.midleft
