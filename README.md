# Pysole documentation
## Introduction

Pysole is a graphical console simulation pygame wrapper or in simpler terms, Pysole uses pygame to simulate a text interface, such as Windows powershell or the Linux Console. Initially Pysole was built to emulate .NET Console Applications with their dynamic text and background colouring. However, .NET Console Applications, without the support of mono cannot run on operating systems other then windows. Pysole can run on any os that python and pygame can.

## Table of contents
1. [Download](#download)
2. [How to use](#how-to-use)
3. [Colours](#colours)
4. [Configuration](#configuration)
5. [Images](#images)
6. [Authors](#authors)
7. [Planned features](#planned-features)
8. [Known bugs](#known-bugs)
9. [Source file overview](#source-file-overview)

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
config = {'font': 'font.ttf'}

console = console.Console()
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

##Colours
The ConsoleColour class contains a list of named colours and their RGB values. In order to use this class you must import the colour module.

```python
from pysole.colour import ConsoleColour


print(ConsoleColour.olive_drab)
>>> (107, 142, 45)
```

Any RGB value in the form of a tuple can be passed as a colour for example:

```python
console.foreground_color = ConsoleColour.navajo_white
```

Is the exact same as:

```python
console.foreground_color = (255, 222, 173)
```

## Configuration
To customise the initial Console a configuration dictionary can be added to the Console. An example:

```python
config = {'title': 'Pysole', 'resizeable': True, 'font': 'font.ttf'}

console = console.Console(config)
```

Here are all the configuration keywords and what values they should be.

```python
'title':                     [string]         # The caption for the window.
'icon':                      [string]         # The icon for the window.
'fps':                       [int]            # Frames per second.
'line_cutoff':               [int]            # How many lines should be in the buffer at any given time?
'default_background_colour': [ConsoleColour]  # The default background colour for the console, used for the reset_colour function as well.
'default_foreground_colour': [ConsoleColour]  # The default foreground colour for the console, used for the reset_colour function as well.
'default_width':             [int]            # Default width of the window.
'default_height':            [int]            # Default height of the window.
'default_min_width':         [int]            # The minimum width of the window.
'default_min_height':        [int]            # The minimum height of the window.
'default_max_width':         [int]            # The maximum width of the window.
'default_max_height':        [int]            # The maximum height of the window.
'resizeable':                [bool]           # Should the window be resizeable?
'beep_sound':                [string]         # Sound the console plays in the beep method.
'font':                      [string]         # Font for the console to use.
'font_size':                 [int]            # Font size.
```

##Images

![alt text](https://github.com/TreeStain/pysole/blob/master/docs/static/img-1.png "Image 1")

![alt text](https://github.com/TreeStain/pysole/blob/master/docs/static/img-2.png "Image 2")

![alt text](https://github.com/TreeStain/pysole/blob/master/docs/static/img-3.png "Image 3")

##Authors

Currently the list of authors is very short (1 person)

* Tristan Arthur (RGSStudios@outlook.com)

##Planned features

Here is a list of all the planned features that are potentially going to be implemented as well as they're priority levels.

* Copy/Cut/Paste
* Text Wrapping
* Shift Variations for characters ✔
* Control Variations
* Scrolling ✔
* Scrolling - Mem Saving ✔
* Column & Row selection
* Changing fonts
* Dynamic font sizes
* Colour enumeration
* Event Handling
* Frame saving
* Hide & Show window ✔
* OS Flavours and default fonts
* Debug/Verbose Output
* Get height and width in rows and columns
* Sleep/Wait function ✔
* Caps lock support
* Newline parsing

## Known bugs

* Scroll uses top as anchor instead of bottom
* Hiding and then showing the window crashes python

##Source file overview
