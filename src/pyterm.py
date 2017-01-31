'''Pyterm module initially created by Tristan Arthur

Pyterm is a pygame wrapper for simulating C# console applications.

To expand, pyterm uses pygames graphics capabilities in an attempt to standardize
text output through a terminal or console. For example, in order to write a
console application that supports colours for windows, you must use C#, however
to do the same thing on a linux system, curses/ncurses is needed. Pyterm escapes
this issue. Thus if a console application that supports colours is needed as well
as support for multiple operating systems, use pyterm.

Extended documentation can be found at treestain.github.io/pyterm/

Classes:
    Terminal: Acts as an abstraction to the window class.

Exceptions:
    TerminalError: Used for more unique and readable error messages.
'''


from colour import ConsoleColour
from window import *


class TerminalError(Exception):
    def __init__(self, message):
        self.message = message

class TerminalConfigError(Exception):
    def __init__(self, message):
        self.message = message

class Terminal:
    def __init__(self, config=None):
        '''Initialises a terminal object and an inner display object.

        Keyword arguments:
        title -- The title of the window.
        icon -- The icon of the window.
        '''

        # Fixed window size config
        self._config = {'title': 'Pyterm',
                        'icon': 'assets/icon.png',
                        'fps': 60,
                        'line_cutoff': 150,
                        'default_background_colour': ConsoleColour.black,
                        'default_foreground_colour': ConsoleColour.white,
                        'default_width': 500,
                        'default_height': 300,
                        'default_min_width': 500,
                        'default_min_height': 300,
                        'font': None
        }

        if config is not None:
            self.change_config(config)

        self.background_color = self._config['default_background_colour']
        self.foreground_color = self._config['default_foreground_colour']

        self.title = self._config['title']
        self.icon = self._config['icon']
        self._fps = self._config['fps']
        self._display = Display(self.title, self._fps, self.icon,
                                size=(self._config['default_width'],
                                      self._config['default_height']),
                                min_size=(self._config['default_min_width'],
                                          self._config['default_min_height']))

        self.default_font = Font("assets/windows.ttf", 15)
        self.row_height = self.default_font.font.size('s')[0]
        self.col_width = self.default_font.font.size('s')[0]

        self._row = 0
        self._column = 0

        self._frame = []
        self._core_update()

        # Hack for write() method to help read_line method character spacing
        self._write_buffer = ["", 0]

    def change_config(self, config):
        for k in config.keys():
            try:
                if self._config[k]:
                    self._config[k] = config[k]
            except KeyError:
                raise TerminalConfigError('An invalid key was provided.')

    def _core_update(self):
        '''Completes one frame of the display'''
        self._display.step(self.background_color)
        for text in self._frame:
            self._display.display_text(text)
        self._display.update()

    def _trim_lines(self, size):
        '''Deletes lines from the start of the frame to the value of size'''
        if len(self._frame) > size:
            i = 0
            while i < len(self._frame) - size:
                self._frame.remove(self._frame[i])
                i += 1

    def _check_write_bounds(self):
        '''Scroll function, will scroll if text is going off screen'''
        col_height = self._row * self.default_font.font.size('s')[1]
        win_height = self._display.height

        if col_height >= win_height:
            for cs in self._frame:
                cs.pos[1] -= self.default_font.font.size('s')[1]
            self._row -= 1

        self._trim_lines(self._config['line_cutoff'])

    def get_size(self):
        return (self._display.width // self.col_width, self._display.height // self.row_height)

    def write_line(self, text=""):
        '''Writes text to the display with a new line.'''
        self._frame += [CharacterString(text, self.default_font,
                                       (self._column * self.default_font.font.size(self._write_buffer[0])[0],
                                        self._row * self.default_font.font.size(self._write_buffer[0])[1]),
                                        self.foreground_color)]
        self._row += 1
        self._column = 0
        self._write_buffer = ["", 0]
        self._check_write_bounds()
        self._core_update()

    def write(self, text):
        '''Writes text to display'''
        self._write_buffer[0] += str(text)
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
        self._check_write_bounds()
        self._core_update()

    def clear(self):
        '''Clears the display.'''
        self._frame.clear()
        self._row = 0
        self._column = 0

    def beep(self):
        '''Sounds a small alert beep'''
        self._display.beep()

    def reset_color(self):
        '''Resets console colour to default colours'''
        self.background_color = self._config['default_background_colour']
        self.foreground_color = self._config['default_foreground_colours']

    def read(self):
        pass

    def read_key(self, wait=True):
        '''Reads a single key from user input'''
        key = self._display.get_key()
        if wait:
            while key is None:
                self._core_update()
                key = self._display.get_key()
        self._core_update()
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

    def sleep(self, ms):
        time = self._display.get_run_time()
        cur_time = time
        while cur_time <= time + ms:
            cur_time = self._display.get_run_time()
            self._core_update()

    def hide(self):
        self._display.quit(full_quit=False)
        self._display = None

    def show(self):
        self._display = Display(self.title, self._fps, self.icon)

    def quit(self):
        '''calls the display quit function'''
        self._display.quit()

if __name__ == '__main__':
    config = {'title': 'Pyterm.py test'
    }

    c = Terminal(config)
    #c.sleep(4000)
    c.write_line('C:\\Users\\RGSSt\\pyterm\\src>git status')
    while True:
        k = c.read_key(wait=False)
        if k is not None:
            print(k)
        if k == '~':
            c.hide()
            break

    c.show()

    c.clear()

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
    c.write_line('Changes not staged or commit:')
    c.write_line('  (use "git add <file>..." to update what will be committed)')
    c.write_line('  (use "git checkout -- <file>..." to discard changes in working directory)')
    c.write_line()
    c.foreground_color = ConsoleColour.red
    c.write_line('        modified:   ../docs/index.html')
    c.foreground_color = ConsoleColour.white
    c.write_line()
    c.write_line()
    c.write_line('C:\\Users\\RGSSt\\pyterm\\src>')

    for i in range(20):
        c.write(i)

    c.read_key()
    c.quit()
