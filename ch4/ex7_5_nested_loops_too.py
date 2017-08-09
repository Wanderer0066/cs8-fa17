#!/usr/bin/python3
import random

# Loops can also be used to do some pretty cool things with output.
rows = int(input('How many rows do you want? '))
max_columns = int(input('What is the maximum number of columns? '))

# This is going to iterate once from 0 to rows -1 (rows times)
for r in range(rows):
    # We'll randomly pick a number of columns from 1 to max_columns
    for c in range(random.randint(1, max_columns)):
        # Notice how are using the end named argument.
	# This will prevent us from moving to a new line after each print
        print('=', end='')
    # Now, outside of the inner loop, print an empty string to advance the line
    print('')
