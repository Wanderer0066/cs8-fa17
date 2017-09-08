#!/usr/bin/python3

country = 'United States'

# The + operator joins strings together.
# The result can be stored in a new string variable
long_country = country + ' of America'

print('country: {}, long_country: {}'.format(
    country, long_country))

# Using the * operation repeats a string
star = '*'
print('5 star: {}'.format(star * 5))

# The first index of a string is 0
print('The first character of country is', country[0])

# The last index of a string will always be len(s) - 1
print('The last character of long_country is', long_country[len(long_country) - 1])
# A shortcut to get the last character is to use -1 as the index value
print('The last character of long_country using -1 is', long_country[-1])
