import random
import os
import pygame as pg

from sprites.bluetank import BlueTank
from sprites.redtank import RedTank
from sprites.explosion import Explosion
from sprites.shot import Shot
from sprites.score import Score
from sprites.wall import Wall
from config.settings import SCREENRECT, MAX_SHOTS
from utils.load import load_image, load_sound

if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

# game constants
SCORE = 0
black = (0,0,0)

main_dir = os.path.split(os.path.abspath(__file__))[0]

def main(winstyle=0):

    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

    fullscreen = False

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # decorate the game window
    icon = pg.transform.scale(load_image("blue-tank-2.png"), (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Tanks")
    pg.mouse.set_visible(0)

    # create the background, tile the bgd image
    background = pg.Surface(SCREENRECT.size)
    background.fill(black)
    screen.blit(background, (0, 0))
    pg.display.flip()

    # load the sound effects
    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("car_door.wav")
    if pg.mixer:
        music = os.path.join(main_dir, "resources", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    # Initialize Game Groups
    walls = pg.sprite.Group()
    shots = pg.sprite.Group()
    tanks = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()

    # assign default groups to each sprite class
    Wall.containers = walls, all
    Shot.containers = shots, all
    BlueTank.containers = tanks, all
    RedTank.containers = tanks, all
    Explosion.containers = all
    Score.containers = all

    score = Score()
    bluetank = BlueTank()
    redtank = RedTank()
    Wall()
    Wall()
    Wall()
    
    clock = pg.time.Clock()

    if pg.font:
        all.add(score)

    while score.SCORE < 5:

        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle | pg.FULLSCREEN, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    fullscreen = not fullscreen

        keystate = pg.key.get_pressed()

        all.clear(screen, background)
        all.update()

        # handle blue player input
        direction = keystate[pg.K_w] - keystate[pg.K_s]
        rotation = keystate[pg.K_d] - keystate[pg.K_a]
        bluetank.move(direction, rotation)
        firing = keystate[pg.K_SPACE]
        if not bluetank.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(bluetank.gunpos, bluetank.rotation)
            if pg.mixer:
                shoot_sound.play()
        bluetank.reloading = firing

        # handle red player input
        direction = keystate[pg.K_UP] - keystate[pg.K_DOWN]
        rotation = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
        redtank.move(direction, rotation)
        firing = keystate[pg.K_RETURN]
        if not redtank.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(redtank.gunpos, redtank.rotation)
            if pg.mixer:
                shoot_sound.play()
        redtank.reloading = firing

        # Detect collisions between tanks and walls.
        for wall in pg.sprite.groupcollide(tanks, walls, 0, 0).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(wall)

        # See if shots hit the walls.
        for wall in pg.sprite.groupcollide(shots, walls, 1, 0).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(wall)

        # # See if shots hit the tanks.
        for tank in pg.sprite.groupcollide(shots, tanks, 1, 0).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(tank)
            score.SCORE += 1

        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)

    if pg.mixer:
        pg.mixer.music.fadeout(1000)
    pg.time.wait(1000)
    pg.quit()


# call the "main" function if running this script
if __name__ == "__main__":
    main()
