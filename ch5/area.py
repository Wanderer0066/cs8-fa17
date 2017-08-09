'''
It is useful to provide a docstring (three quotes) at the top of a module.
This module will have some useful area functions for different shapes
'''
import math

def circle_area(radius):
    return math.pi * radius ** 2
    
def square_area(side):
    return side ** 2
    
def rectangle_area(width, height):
    return width * height
