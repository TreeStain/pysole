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

```
import pysole.console
from pysole.colour import ConsoleColour
```

Next you must initialise and store a new Console object. The console object can be initialised with two optional values title and icon.

`console = pysole.Console()`

Now that you have an initialised Console object you are now able to read, write, and change the display of the console.
