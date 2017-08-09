#!/usr/bin/python3
# A Python program can always import modules from its same directory. We'll learn about
# more complicated scenarios later.
import area

def main():
    shape = input('What shape do you want? ')
    if shape == 'circle':
        radius = int(input('What is the radius? '))
        print('Circle with radius {} is {}'.format(radius, area.circle_area(radius)))
    elif shape == 'square':
        side = int(input('What is the length of a side? '))
        print('Square with sides {} is {}'.format(side, area.square_area(side)))
    elif shape == 'rectangle':
        width = int(input('What is the width? '))
        height = int(input('What is the height? '))
        print('Rectangle with width {} and height {} is {}'.format(
            width, height, area.rectangle_area(width=width, height=height)))
    else:
        print('I dunno that shape!')
    
main()