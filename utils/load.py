import os
import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join(main_dir, "..", "resources", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


def load_sound(file):
    """ because pygame can be be compiled without mixer.
    """
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "..", "resources", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None