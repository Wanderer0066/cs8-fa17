#!/usr/bin/python3

# Build a list counting from 1 to 20
list1 = list(range(1, 21))

# This is a basic slice; the 3rd through 6th items
# This is the same as list1[2], list1[3], list1[4], list1[5]
slice1 = list1[2:6]
print('slice1=', slice1)

# If you omit the number before the colon, the slice starts
# from index 0.
slice2 = list1[:6]
print('slice2=', slice2)

# Likewise, if you omit the number after the colon, the slice will
# proceed to the end of the list
slice3 = list1[2:]
print('slice3=', slice3)

# You can omit both pieces to create a full copy of a list. This
# is a commonly used trick by Python programmers
list1_copy = list1[:]
print('list1_copy=', list1_copy)

# You can also use a negative start index to get a slice
# counting backwards from the end of the list.
slice4 = list1[-5:]
print('slice4=', slice4)

# This syntax is a bit more awkward, but it will stop 5 items
# from the end of the list
slice5 = list1[:-5]
print('slice5=', slice5)

# Finally, you can give three slice options seperated by colons
# to provide a 'step' value. This will grab only the even numbers.
evens = list1[1::2]
print('evens=', evens)
