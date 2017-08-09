#!/usr/bin/python3

def main():
  try:
    f = open('ex9_output.txt', 'w')
    # This is a data entry program. We'll stay in loop until a particular sentinel
    # value is retrieved OR when an exception is thrown.
    while True:
      name = input('Enter book name: ')
      # If the user types DONE in all caps, break the loop
      if name == 'DONE':
        break
      price = float(input('Enter book price: '))
      f.write('{}\t{:,.2f}\n'.format(name, price))
  except IOError as ie:
    print(ie)  # Here, we'll print the IOError exception object
  except ValueError as ve:
    print('You have provided bad data!')
    print(ve)
  # finally blocks will execute regardless of whether an exception has occurred or not.
  # Thus, they're a good place to put operations that need to happen no matter what
  # the program has done to this point. Usually, this is where files or DB connections
  # are closed.
  finally:
    print('File will be closed')
    f.close()

main()

