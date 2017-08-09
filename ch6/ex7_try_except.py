#!/usr/bin/python3

def main():
  # Using the try statement block means that every Python statement inside of the block
  # that could throw an exception will be caught and passed to the except block rather
  # than cause the program to halt unexpectedly. This allows you to execute statements
  # that could fail if bad data is passed to them (ie. int() with a non-numeric string).
  try:
    payments = int(input('Enter number of payments you want to make: '))
    loan = float(input('Enter the total loan amount: '))
    payment = loan / payments
    print('Your payment is ${:,.2f}'.format(payment))

  # The except block will catch any ValueError exception throw inside the try block.
  # Both int() and float() could raise ValueErrors so we don't know for certain
  # where the error occurred.
  except ValueError:
    print('One of your inputs is invalid!')
  except ZeroDivisionError:
    print('You cannot have zero payments!')

  print('Program exits normally')


main()
