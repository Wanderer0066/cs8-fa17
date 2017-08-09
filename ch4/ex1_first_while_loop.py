#!/usr/bin/python3

item = ''
total = 0

# As long as total < 3, the statements inside of the while loop
# block will continue to be executed.
while total < 3:
    item = input('What would you like? ')
    total += 1
    print('You now have {} items'.format(total))

# When the conditional test that controls the loop is False, the loop breaks
# and the statement following the while block is executed.
print('Your order is complete')
