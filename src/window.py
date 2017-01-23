"""Universal Terminal Emulator window module.

This module provides core functionality for the ute module, such
as creating, manipulating and destroying windows. It provides the
means to create fonts and render graphics to the screen.

Example:
    $ python3
    >> import Window

Todo:
    * (Tristan Arthur): Fix so input can read CTRL, ETC and display correctly.
    * (Tristan Arthur): Refactor module name from "Window" to "window" to follow standards

"""


import pygame
from pygame.locals import *
from sys import exit


class Font(object):
    """Font class creates a pygame font to be used with rendering text.

    Args:
        font_location (str): Location of font file on disk.
        size (int): Font size

    Attributes:
        font (pygame.font.Font): Font created from font location and size.
        size (int): Font size

    Note:
        A different class from the pygame font class was created to store
        the size as well as the pygame font class.

    """
    def __init__(self, font_location, size):
        self.font = pygame.font.Font(font_location, int(size))
        self.size = size


class CharacterString(object):
    """CharacterString class is a string that can be rendered
    onto a pygame window with a certain font, location and colour.

    Args:
        text (str): Render-able text
        f (Font): Font to use with text
        pos (int tuple): The position in which to render the text at
        col (int tuple): The colour of the text

    Attributes:
        txt_surface (pygame Surface): Surface to be rendered by window class
        text (str): Render-able text
        f (Font): Font to use with text
        pos (int tuple): The position in which to render the text at
        col (int tuple): The colour of the text

    Note:
        This class not only stores the string, but also the position font and
        colour. Furthermore allowing these values to be dynamicaly changed

    """
    def __init__(self, text, f, pos, col=(255, 255, 255)):
        self.txt_surface = None
        self.pos = pos
        self.col = col
        self.f = f
        self.text = text
        self.render()

    def render(self):
        self.txt_surface = self.f.font.render(str(self.text), True, self.col)


class Display(object):
    def __init__(self, title, fps, icon_loc, size=(500, 300), min_size=(500, 300)):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        pygame.display.set_icon(pygame.image.load(icon_loc))

        self.width = size[0]
        self.height =  size[1]

        self._surf = pygame.display.set_mode((self.width, self.height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(title)
        self.min_size = min_size

        self._clock = pygame.time.Clock()
        self._FPS = fps

        # All keys that have been pressed before return
        self._sustained_keys = ""
        # Flag to mark when to remove sk's as return pressed
        self._sk_flag = False

        # Event variable for key down
        self._key_down = None
        # Event variable for return pressed
        self._return_down = False
        # Event variable for backspace pressed\
        self._back_down = False

        self.beep_sound = pygame.mixer.Sound("assets/beep.wav")

    def display_text(self, cs):
        self._surf.blit(cs.txt_surface, cs.pos)

    def step(self, bg):
        self._clock.tick(self._FPS)

        self._surf.fill(bg)

        # Reset key down variables at start of step
        self._key_down = None
        self._return_down = False
        self._back_down = False

        # Check if sk flag triggered and reset sk and sk flag
        if self._sk_flag is True:
            self._sustained_keys = ""
            self._sk_flag = False

        # Key presses
        key_state = pygame.key.get_pressed()
        upper = False
        if key_state[K_LSHIFT]:
            upper = True

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self._return_down = True
                elif event.key == K_BACKSPACE:
                    self._sustained_keys = self._sustained_keys[:-1]
                    self._back_down = True
                elif event.key != K_LSHIFT:
                    if upper:
                        self._key_down = chr(event.key).upper()
                        self._sustained_keys += self._key_down.upper()
                    else:
                        self._key_down = chr(event.key)
                        self._sustained_keys += self._key_down

            # Handle resizing and min window size
            if event.type == VIDEORESIZE:
                self.width, self.height = event.size
                if self.width < self.min_size[0]:
                    self.width = self.min_size[0]
                if self.height < self.min_size[1]:
                    self.height = self.min_size[1]
                self._surf = pygame.display.set_mode((self.width, self.height), HWSURFACE | DOUBLEBUF | RESIZABLE)
                pygame.display.flip()

    def get_key(self):
        # Return key pressed on this frame, return None if no key pressed
        self._sustained_keys = ""
        return self._key_down

    def get_line(self):
        # Return all sk, return pressed event and key pressed this frame
        return [self._sustained_keys, self._return_down, self._key_down, self._back_down]

    def reset_get_line(self):
        # Used after get_line method to reset sk
        self._sk_flag = True

    def beep(self):
        self.beep_sound.play()

    @staticmethod
    def update():
        pygame.display.update()

    @staticmethod
    def quit():
        pygame.font.quit()
        pygame.quit()
        exit()
