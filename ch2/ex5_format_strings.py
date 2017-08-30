#!/usr/bin/python3

# Since Python 2.6, the .format() method of strings is the preferred
# formatting technique
print('{} serve as placeholders'.format('Curly braces'))
print('It is easy to format numbers ${:3,.2f} and {:3.2%}'.format(2325.32, 0.65))

# Formatted strings can be stored in variables
bin_to_dec = '{:b} in binary = {:d} in decimal'.format(128, 128)
print(bin_to_dec)

print('You can pad values to a particular width {:010d}'.format(245))
