#!/usr/bin/python3

# f will be a file object with the name 'ex2_file.txt' and we will open it
# for reading. If the file doesn't exist, Python will throw an exception.
f = open('ex2_file.txt')

# The readline() method will read one line at a time from a file until the
# end is reached where it will return an empty string.
lines_read = 0
line = f.readline()
# Remember, a while loop test condition is True for any non-empty string
while line:
    line = line.rstrip()
    lines_read += 1
    print('Line {}: {}'.format(lines_read, line))

    # In order to prevent an infinite loop, we have to call readline again to
    # prepare for the next conditional test
    line = f.readline()

print('Read', lines_read, 'total lines from file')

# When we're done working with a file object, we need to call its close method.
# Even though we didn't change it, this ensures that no operating system handles
# to the files are left open and that any memory in use can be freed.
f.close()
