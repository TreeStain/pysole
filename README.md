# Pysole documentation
## Introduction

Pysole is a graphical console simulation pygame wrapper or in simpler terms, Pysole uses pygame to simulate a text interface, such as Windows powershell or the Linux Console. Initially Pysole was built to emulate .NET Console Applications with their dynamic text and background colouring. However, .NET Console Applications, without the support of mono cannot run on operating systems other then windows. Pysole can run on any os that python and pygame can.

## Table of contents
1. Download
2. How to use
3. Colours
4. Configuration
5. Images
6. Authors
7. Planned Features
8. Know bugs
9. Source file overview

## Download
* [Github repository](https://github.com/TreeStain/pysole)

Pysole can also be installed with pip and the PyPi using the following command.

`pip install pysole`

## How to use
In order to intergrate your Pysole with your application there is a few steps you must follow. First of all you need to import Pysole. Although it is not necessary you can also import the Colour module, which gives you an enourmouse selection of named colours.

```python
import pysole.console
from pysole.colour import ConsoleColour
```

Next you must initialise and store a new Console object. The console object can be initialised with two optional values title and icon.

```python
console = pysole.Console()
```

Now that you have an initialised Console object you are now able to read, write, and change the display of the console.

```python
# Console write, writes the text you parse it without a newline at the end of the string.
console.write('Hello World')

# Console write line does the same as write except with a newline at the end.
console.write_line(', this is a console')

# Console clear, clears the frame and removes all text from the console display buffer.
console.clear()

# Console read line returns all the input of a user until they press return.
name = console.read_line('What is your name? ')

# Console read key returns a single user key press.
key = console.read_key()
```

In order to change the colours of the text and background all that needs to be done is to change the console variables foreground_color and background_color

```python
console.foreground_color = ConsoleColour.red
console.background_color = ConsoleColour.white

# The reset colour method resets the console colours back to the defaults.
console.reset_color()
```

If you, for whatever reason, need to use audio cue the Console beep method can be used.

```python
console.beep()
```

To quit pysole and close the window the following statement must be used.

```python
console.quit()
```
