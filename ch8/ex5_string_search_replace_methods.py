#!/usr/bin/python3

user_data = input('Give me some data! ')

if user_data.endswith('!'):
  print('Hey no need for shouting')

if user_data.startswith('#'):
  print('Hope this trends!')


# The find method is unique to strings. Its similar
# to the index method except it does not throw a ValueError
# when it fails to find the value given as an argument. It
# will instead return -1.
if user_data.find('secret') > -1:
  # Remember, replace doesn't change the string.
  # It will only return a copy so if you want to use it,
  # you need to assign it to a new variable
  new_code = user_data.replace('secret', '*****')
  print('"{}" -> "{}"'.format(user_data, new_code))
else:
  print('Your input did not contain the code')
