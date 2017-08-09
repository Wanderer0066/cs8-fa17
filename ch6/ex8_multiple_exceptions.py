#!/usr/bin/python3

def main():
  # The code below could raise a number of different exceptions, so our try block is
  # followed by except blocks to handle all of them.
  try:
    filename = input('Where is the data file? ')
    f = open(filename)
    total = 0
    for l in f:
      total += float(l.rstrip())

    print('The sum total of the file is ${:,.2f}'.format(total))
  except IOError:
    print('"{}" could not be opened. Are you sure it exists?'.format(filename))
  except ValueError:
    print('A record from "{}" is corrupt'.format(filename))
  # We could comment out the except clauses above and only leave the following generic,
  # untyped except block. This catches any and all kinds of errors but makes it more
  # challenging to know exactly what went wrong to give the user meaningful feedback.
  except:
    print('An unknown error occurred')


main()
