"""Universal Terminal Emulator ute module.

This module acts as the controller for the window module and abstracts all low level
activity from the user. If the window module was a set of tools the ute module is
instructions on how to use those tools.

Example:
    $ python3
    >> import ute
    >> c = ute.Console(title="Console", icon="icon.png")

Todo:
    * (Tristan Arthur): Add documentation and commenting
    * (Tristan Arthur): Add screen scrolling for when text goes off screen
    * (Tristan Arthur): Copy, paste, cut text, good luck xD

"""


from colour import ConsoleColour
from window import *


class Terminal(object):
    def __init__(self, title="Universal Terminal Emulator", icon="assets/icon.png"):

        self.background_color = ConsoleColour.black
        self.foreground_color = ConsoleColour.white

        self.title = title
        self._fps = 60
        self._display = Display(self.title, self._fps, icon)

        self.default_font = Font("assets/windows.ttf", 15)

        self._row = 0
        self._column = 0

        self._frame = []
        self._core_update()

        # Hack for write() method to help read_line method character spacing
        self._write_buffer = ["", 0]

    def _core_update(self):
        '''Completes one full cycle of the window loop including, step, display and update'''
        self._display.step(self.background_color)
        for line in self._frame:
            self._display.display_text(line)
        self._display.update()


    def write_line(self, text=""):
        '''Writes a text to output and then increments row by 1'''
        self._frame += [CharacterString(text, self.default_font,
                                       (self._column * self.default_font.font.size(self._write_buffer[0])[0],
                                        self._row * self.default_font.font.size(self._write_buffer[0])[1]),
                                        self.foreground_color)]
        self._row += 1
        self._column = 0
        self._write_buffer = ["", 0]
        self._core_update()

    def write(self, text):
        '''Writes text to output'''
        self._write_buffer[0] += text
        try:
            if self._write_buffer[1] != 0:
                self._frame.pop()
        except IndexError:
            pass
        self._frame += [CharacterString(self._write_buffer[0], self.default_font,
                                       (self._column * self.default_font.font.size(self._write_buffer[0])[0],
                                        self._row * self.default_font.font.size(self._write_buffer[0])[1]),
                                        self.foreground_color)]

        self._write_buffer[1] += 1
        self._core_update()

    def clear(self):
        '''Clears the frame buffer, thus clearing the screen of text'''
        self._frame.clear()
        self._row = 0
        self._column = 0

    def beep(self):
        '''Sounds a small alert beep'''
        self._display.beep()

    def reset_color(self):
        '''Resets console colour to default colours'''
        self.background_color = ConsoleColor.black
        self.foreground_color = ConsoleColor.white

    def read(self):
        pass

    def read_key(self):
        '''Reads a single key from input stream and returns it'''
        key = self._display.get_key()
        while key is None:
            self._core_update()
            key = self._display.get_key()
        return key

    def read_line(self, for_text=""):
        '''Reads text constantly until 'enter' has been pressed and returns it'''
        if for_text != "":
            self.write(for_text)
        line = self._display.get_line()
        while line[1] is False:
            self._core_update()
            line = self._display.get_line()
            if line[2] is not None:
                self.write(line[2])
            if line[3]:
                # Handle backspacing, very hacky
                self._write_buffer[0] = self._write_buffer[0][:-1]
                self._write_buffer[1] -= 1
                self.write('')
        self._write_buffer = ["", 0]
        self._display.reset_get_line()
        self._row += 1
        return line[0]

    def quit(self):
        '''calls the display quit function'''
        self._display.quit()

if __name__ == '__main__':
    c = Terminal(title='pyterm.py test')

    c.write_line()
    c.write_line('C:\\Users\\RGSSt\\pyterm\\src>git status')
    c.write_line('On branch master')
    c.write_line('Your branch is up-to-date with \'origin/master\'.')
    c.write_line('Changes to be committed:')
    c.write_line('  (use "git reset HEAD <file>..." to unstage)')
    c.write_line()
    c.foreground_color = ConsoleColour.green
    c.write_line('        modified:    pyterm.py')
    c.foreground_color = ConsoleColour.white
    c.write_line()
    c.write_line('Changes not staged for commit:')
    c.write_line('  (use "git add <file>..." to update what will be committed)')
    c.write_line('  (use "git checkout -- <file>..." to discard changes in working directory)')
    c.write_line()
    c.foreground_color = ConsoleColour.red
    c.write_line('        modified:   ../docs/index.html')
    c.foreground_color = ConsoleColour.white
    c.write_line()
    c.write_line()
    c.write_line('C:\\Users\\RGSSt\\pyterm\\src>')

    c.read_key()
    c.quit()
