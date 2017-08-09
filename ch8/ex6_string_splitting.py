#!/usr/bin/python3

# When you use .split(), you will always get a list object
# back. Each member of the list will be a string.

sentence = 'The cow jumped over the moon.'
# With no arguments given, split will break up a string
# into pieces at each occurence of a white space.
words = sentence.split()
# Words is a list
print('split by default', words)

# You can also give an argument to split and it will use
# that as the split character.
words = 'John Doe:Male:8/15/1982'.split(':')
print('split by colon', words)

# If the split character you give cannot be found, you
# will get a list containing one entry, the original string
words = 'There_are_no_spaces_here'.split()
print('split no occurences', words)

# Splits can be very useful when reading data from files
# which we'll learn next chapter. You can then treat str
# data from numeric data differently.
car_bill =  'Car Payment,350.00'
electric_bill = 'Electric,120.97'

pieces = car_bill.split(',')
payee = pieces[0]
late_amount = float(pieces[1]) * 1.10  # 10%
print('Late Bill for "{}" is ${:.2f}'.format(payee, late_amount))

pieces = electric_bill.split(',')
payee = pieces[0]
late_amount = float(pieces[1]) * 1.10  # 10%
print('Late Bill for "{}" is ${:.2f}'.format(payee, late_amount))
