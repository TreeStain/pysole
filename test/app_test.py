#!/usr/bin/env python3

from colour import ConsoleColour
import pyterm



c = UTE.Terminal(title="DEBUG: Universal Terminal Emulator", icon="icon.png")


def main():
    c.read_key()
    c.quit()


def colour_text(text, cc):
    c.foreground_color = cc
    c.write_line(text)
    c.reset_color()

if __name__ == "__main__":
    main()
