#!/usr/bin/python3

# f will be a file object with the name 'ex2_file.txt' and we will open it
# for reading. If the file doesn't exist, Python will throw an exception.
f = open('ex2_file.txt')

# This is the simplest and most commonly used means for reading a file
# line-by-line in Python. The loop iteration variable line will get set to
# each successive line in the file (including the new line character).
lines_read = 0
for line in f:
    lines_read += 1
    print('Line {}: {}'.format(lines_read, line.rstrip()))

print('Read', lines_read, 'total lines from file')

# When we're done working with a file object, we need to call its close method.
# Even though we didn't change it, this ensures that no operating system handles
# to the files are left open and that any memory in use can be freed.
f.close()
