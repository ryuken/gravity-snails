import pygame
import os
import sys
from pygame.locals import *

def load_image(name, colorkey=None):
    """loads an image into memory"""
    fullpath = os.path.abspath(os.path.dirname(sys.argv[0]))
    fullname = fullpath + '/sprites/'
    fullname = fullname + name
    #print(fullname + "\n")
    try:
        image = pygame.image.load(fullname)
    except (pygame.error, message):
        print('Cannot load image:', fullname)
        raise (SystemExit, message)
    #image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def load_sound(name):
    """loads a sound file (.wav) in memory"""
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullpath = os.path.abspath(os.path.dirname(sys.argv[0]))
    fullname = fullpath + '/sounds/'
    fullname = fullname + name
    print(fullname + "\n")
    try:
        sound = pygame.mixer.Sound(fullname)
    except (pygame.error, message):
        print('Cannot load sound:', fullname)
        raise (SystemExit, message)
    return sound
