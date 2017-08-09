#!/usr/bin/python3

# Here we create a dict object to represent the Pittsburgh Pirates team.
team = {
  'P': 'Gerrit Cole',
  '1B': 'Josh Bell',
  '2B': 'Josh Harrison',
  'SS': 'Jordy Mercer',
  '3B': 'David Freese',
  'LF': 'Starling Marte',
  'CF': 'Andrew McCutchen',
  'RF': 'Gregory Polanco',
  'C': 'Francisco Cervelli',
  'Manager': 'Clint Hurdle',
  'wins': 78,
  'losses': 83
}

# The in operator lets us check for a key and can be used in a boolean
# expression. This is often used to check for a key before trying to access or
# change the value associated with it.
if 'P' in team:
  print('The Pirates pitcher is', team['P'])

# The not in operator performs the inverse operation. If a key is not found, it
# returns true. This is often used to initialize a key's value for the first
# time it is encountered (such as when reading through a file).
if 'Closer' not in team:
  team['Closer'] = 'Tony Watson'
  print('The Pirates Closer is', team['Closer'])

# Just like items at list indices, a value associated with a key can be any
# Python type such as lists, tuples, or even other dicts.
team['last3games'] = ['CIN', 'CIN', 'CHI']
team['info'] = {'city': 'Pittsburgh', 'name': 'Pirates', 'payroll': 100000000}

print('Team', team)

# The del keyword allows us to remove an item specified by its key.
del team['3B']
print('Team after retirement', team)
