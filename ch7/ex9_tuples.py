#!/usr/bin/python3

# Tuples are often used for module variables which are
# typically intended to be read-only anyways.
VALID_COMMANDS = (
  'Speak',
  'Sit',
  'Lie down'
)

prompt = 'I am dog, what should I do? '
command = input(prompt)
while command != 'DONE':
  if command in VALID_COMMANDS:
    print('Ok, I will', command)
  else:
    print("I don't know that one")
  command = input(prompt)

# You can index a particular item, but you cannot change it
print(VALID_COMMANDS[0])
#VALID_COMMANDS[0] = 'Bark'

# You can convert a tuple to a list and back if you want
commands_list = list(VALID_COMMANDS)
commands_list[0] = 'Bark'
commands_tuple = tuple(commands_list)
print('commands_tuple=', commands_tuple)
