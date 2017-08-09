#!/usr/bin/python3

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
email = input('What is your email address? ')
major = input('What is your major? ')
standing = input('What is your class standing? ')

print('=' * 80)
print('= Name: {}, {} | Email: {}'.format(last_name, first_name, email))
print('= Major: {} | Class: {}'.format(major, standing))
print('=' * 80)
