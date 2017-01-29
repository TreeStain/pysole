import pyterm
from colour import ConsoleColour
from random import randint


console = pyterm.Terminal(title='Matrix')
console.foreground_color = ConsoleColour.green

while True:
    line = ''
    for i in range(console.get_size()[0]):
        line += str(randint(0, 1))
    console.write_line(line)
