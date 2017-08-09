#!/usr/bin/python3

# Here we create a dict object to represent the Pittsburgh Pirates team.
team = {
  'P': 'Gerrit Cole',
  '1B': 'Josh Bell',
  '2B': 'Josh Harrison',
  'SS': 'Jordy Mercer',
  '3B': 'Davod Freese',
  'LF': 'Starling Marte',
  'CF': 'Andrew McCutchen',
  'RF': 'Gregory Polanco',
  'C': 'Francisco Cervelli',
  'Manager': 'Clint Hurdle',
  'wins': 78,
  'losses': 83
}

# The basic for/in loop allows us to loop over a dictionary's keys and then
# be able to access its values.
print('====================  Using loops with dicts ====================')
for k in team:
  # Remember, k is going to get assigned to a key from team in arbitrary order.
  # If we want the value associated with key, we need to use square-bracket
  # notation.
  print('{}={}'.format(k, team[k]))


# the .get() method accepts two arguments, the name of the key to lookup
# and a default value if it's not found.
print('====================  .get() method ====================')
print('The SS is', team.get('SS', 'Vacant'))
print('The Closer is', team.get('Closer', 'Vacant'))

# The .keys, .values, and .items methods return sequences that you can convert
# to lists.
print('====================  .keys() method ====================')
keys = team.keys()
print(list(keys))

print('====================  .values() method ====================')
# .values() returns a copy of the actual values. Changing these will not change
# the underlying dict's values.
values = team.values()
print(list(values))

print('====================  .items() method ====================')
# .items() returns a copy of the actual values. Changing these will not change
# the underlying dict's values unless you use the dict_obj[key] square-bracket
# syntax.
items = team.items()
print(list(items))

# .items can be used with a unique form of the for loop that assigns two loop
# variables at once.
print('====================  Loop with .items() method ====================')
for k, v in team.items():
  print('{}={}'.format(k, v))

# .clear wipes out everything in the dict resetting it to its empty state.
team.clear()
print('After .clear()', team)


