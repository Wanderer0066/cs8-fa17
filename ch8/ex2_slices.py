#!/usr/bin/python3

# Build a list counting from 1 to 20
my_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# This is a basic slice; the 3rd through 6th items
# This is the same as my_str[2] + my_str[3] + my_str[4] + my_str[5]
slice1 = my_str[2:6]
print('slice1=', slice1)

# If you omit the number before the colon, the slice starts
# from index 0.
slice2 = my_str[:6]
print('slice2=', slice2)

# Likewise, if you omit the number after the colon, the slice will
# proceed to the end of the string starting from the first index
slice3 = my_str[2:]
print('slice3=', slice3)

# You can also use a negative start index to get a slice
# counting backwards from the end of the string.
slice4 = my_str[-5:]
print('slice4=', slice4)

# This syntax is a bit more awkward, but it will stop 5 items
# from the end of the str
slice5 = my_str[:-5]
print('slice5=', slice5)

# Finally, you can give three slice options seperated by colons
# to provide a 'step' value. This will grab every other letter
# starting at B
every_other = my_str[1::2]
print('every_other=', every_other)
