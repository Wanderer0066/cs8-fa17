#!/usr/bin/python3

# This is the simplest form of a for loop. Notice the use of the variable name
# 'i', the keyword 'in', and the sequence of values inside of square brackets,
# [1, 2, 3]. The values in brackets are a Python list which will discuss 
# in more detail later.
for i in [1, 2, 3]:
    # This loop while cause the print statement to execute 3 times; once for 
    # each value of i.
    print('This is the {} time through'.format(i))
