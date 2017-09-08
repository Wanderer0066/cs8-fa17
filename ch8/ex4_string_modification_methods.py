#!/usr/bin/python3

user_data = input('Give me some data! ')

a = user_data.lower()
print('Lowercase is "{}"'.format(a))
a = user_data.upper()
print('Uppercase is "{}"'.format(a))
a = user_data.strip()
print('Stripped of all leading and trailing whitespace is "{}"'.format(a))
a = user_data.strip('-')
print('Stripper of leading and trailing dashes is "{}"'.format(a))
