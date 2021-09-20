import pygame as pg

from sprites.tank import Tank
from utils.load import load_image
from config.settings import SCREENRECT

class BlueTank(Tank):
    def __init__(self):
        self.images = [load_image(im) for im in ("blue-tank-0.png", "blue-tank-1.png", "blue-tank-2.png", "blue-tank-3.png", "blue-tank-4.png", "blue-tank-5.png", "blue-tank-6.png", "blue-tank-7.png" )]
        self.image = self.images[2]
        self.rotation = 90
        Tank.__init__(self, 0)
        self.move(0, 0)
