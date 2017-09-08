#!/usr/bin/python3

user_data = input('Give me some data! ')

if user_data.isalnum():
  print(user_data, 'contains only letters and numbers.')

if user_data.isalpha():
  print(user_data, 'contains only letters.')

if user_data.isdigit():
  print(user_data, 'contains only numbers.')

if user_data.islower():
  print(user_data, 'contains only lowercase letters')

if user_data.isupper():
  print(user_data, 'contains only uppercase letters')

if user_data.isspace():
  print(user_data, 'contains only whitespace')
