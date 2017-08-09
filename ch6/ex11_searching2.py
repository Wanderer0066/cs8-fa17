#!/usr/bin/python3

def main():
  # Get some basic details from the user
  filename = input('What file contains the data you want to search? ')
  needle = input('What string do you want to search for? ')
  try:  
    f = open(filename)
    
    # Read the file line by line
    lines_read = 0
    # This approach will be slightly different, We'll store a list of tuples
    # where the first item in each tuple is the line number and the second
    # is the position in the line
    found_at = []
    for line in f:
      lines_read += 1
      # Remember, the .find method of a string returns the starting index
      # of the argument in the string object that the method is called on
      # or -1 if it's not found
      position = line.find(needle)
      if position > -1:
        found_at.append((lines_read, position))
    
    # An non-empty list evaluates to True when used in an if clause, so we can
    # check to see if found_at has any members and then iterate through them
    # to display our results.
    if found_at:
      print('Found "{}" at:'.format(needle))
      for t in found_at:
        print('\tLine {}, position {}'.format(t[0], t[1]))    
    else:
      print('Did not find "{}" anywhere in the file'.format(needle))
        
    f.close()
  except IOError:
    print('"{}" cannot be opened for reading'.format(filename))

main()

