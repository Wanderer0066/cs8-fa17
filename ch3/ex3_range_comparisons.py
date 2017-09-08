#!/usr/bin/python3

temperature = int(input('What is the temperature today? '))
message = ''

if temperature > 90:
  message = 'Wow, it is super hot'
elif temperature > 80:
  message = "It's pretty toasty"
elif temperature > 70:
  message = 'What a nice summer day'
elif temperature > 50:
  message = 'A cool, crisp one'
elif temperature > 30:
  message = 'Staying above freezing...barely'
elif temperature <= 30:
  message = 'Welcome to winter, stay inside'

print(message)

