#!/usr/bin/python3
# Let's try some input

name = input('Enter your name: ')
# This won't work if we want age to be a numeric value
#age = input('Enter your age: ')
age = int(input('Enter your age: '))

print('Your name is', name, 'and you are', age)

ten_years_age = age + 10
print('In 10 years, you will be', ten_years_age)
