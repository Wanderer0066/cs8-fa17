#!/usr/bin/python3

def main():
  # Get some basic details from the user
  filename = input('What file contains the data you want to search? ')
  needle = input('What string do you want to search for? ')
  try:
    f = open(filename)

    # Read the file line by line
    lines_read = 0
    # You'll typically want to use a found flag to indicate
    # that the search was successful. You won't know if the data is present
    # until you've processed every single item.
    found = False
    for line in f:
      lines_read += 1
      # Remember, the .find method of a string returns the starting index
      # of the argument in the string object that the method is called on
      # or -1 if it's not found
      position = line.find(needle)
      if position > -1:
        print('Found "{}" at position {} in line {}'.format(
          needle, position, lines_read))
        found = True
        # The break statement will exit the loop and move to the
        # statement following it
        break

    if not found:
      print('Did not find "{}" anywhere in the file'.format(needle))

    f.close()
  except IOError:
    print('"{}" cannot be opened for reading'.format(filename))

main()

