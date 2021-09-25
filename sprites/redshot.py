import pygame as pg

from sprites.shot import Shot

class RedShot(Shot):
    def __init__(self, pos, rotation):
        Shot.__init__(self, pos, rotation)
