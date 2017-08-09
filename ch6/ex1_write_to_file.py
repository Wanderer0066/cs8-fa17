#!/usr/bin/python3

# f will be a file object with the name 'ex1_file.txt' and we will open it
# for writing. If the file doesn't exist, Python will create it.
f = open('ex1_file.txt', 'w')
f.write('This is the first line of my file\n')
f.write('If I want output to be on a new line, I have to add it explicitly')
f.write(', otherwise the output will stay on the same line.\n')

# When we're done working with a file object, we need to call its close method
# to ensure that all changes are written to disk.
f.close()
