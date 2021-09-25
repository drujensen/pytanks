import pygame as pg

from config.settings import SCREENRECT

class Score(pg.sprite.Sprite):
    SCORE = 0
    buffer = 10
    def __init__(self, leftside = True):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = pg.Color("white")
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect()
        if leftside:
            x = self.buffer
        else:
            x = SCREENRECT.width - self.rect.width - self.buffer
        y = SCREENRECT.height - self.rect.height - self.buffer
        self.rect.move_ip(x, y)

    def update(self):
        if self.SCORE != self.lastscore:
            self.lastscore = self.SCORE
            msg = "Score: %d" % self.SCORE
            self.image = self.font.render(msg, 0, self.color)
