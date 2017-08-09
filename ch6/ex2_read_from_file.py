#!/usr/bin/python3

# f will be a file object with the name 'ex2_file.txt' and we will open it
# for reading. If the file doesn't exist, Python will throw an exception.
f = open('ex2_file.txt')

# The .read method returns the entire files contents all at once in a string.
# This includes the new lines so it's not often useful for multi-line files.
full_contents = f.read()
print('--- Contents from ex2_file.txt ---')
print(full_contents)
print('--- End Contents ---')

# When we're done working with a file object, we need to call its close method.
# Even though we didn't change it, this ensures that no operating system handles
# to the files are left open and that any memory in use can be freed.
f.close()