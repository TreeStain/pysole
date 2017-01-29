#!/usr/bin/env python3

import pyterm
from colour import ConsoleColour
from random import randint


c = pyterm.Terminal(title="Math Game")


def main():
    num_correct = 0
    num_incorrect = 0
    while num_correct < 11:
        n1, n2 = randint(0, 50), randint(0, 50)
        ans = n1 + n2
        user_ans = c.read_line("{x} + {y} = ".format(x=n1, y=n2))
        if user_ans == str(ans):
            num_correct += 1
            c.foreground_color = ConsoleColour.green
            c.write_line("Correct")
        else:
            num_incorrect += 1
            c.foreground_color = ConsoleColour.red
            c.write_line("Incorrect")
        c.reset_color()

if __name__ == "__main__":
    main()
