#!/usr/bin/python3

teams = [
  'Atlanta Falcons',
  'Baltimore Ravens',
  'Boston Patriots',
  'Buffalo Bills',
  'Charlotte Panthers',
  'Chicago Bears',
  'Cincinatti Bengals',
  'Cleveland Browns',
  'Dallas Cowboys',
  'Denver Broncos',
  'Detroit Lions',
  'Indianapolis Colts',
  'Jacksonville Jaguars',
  'Kansas City Chiefs',
  'Miami Dolphins',
  'Green Bay Packers',
  'Minneapolis Vikings',
  'Nashville Titans',
  'New Orleans Saints',
  'New York Giants',
  'New York Jets',
  'Oakland Raiders',
  'Philadelphia Eagles',
  'Phoenix Cardinals',
  'Pittsburgh Steelers',
  'St Louis Rams',
  'San Diego Chargers',
  'San Francisco 49ers',
  'Seattle Seahawks',
  'Tampa Buccaneers',
  'Washington Redskins',
  'Houston Texans'
]

# .append lets us add an item to the end of a list
teams.append(input('Enter the expansion team city and name: '))
print(teams[-1])  # Remember, -1 will show us the last item added
print('---------------------------------------------------------------------')

# .insert lets us add an item at a particular position. All other
# items will be shifted down accordingly. The first argument is
# the position we wish to add the item at, the second argument is
# the item itself.
teams.insert(0, 'Los Angeles Stars')
print('Teams after expansions:', teams)
print('---------------------------------------------------------------------')

# A list can be sorted in place by using the .sort method.
# This will use lexographic sorting which is usually the same
# as alphabetical unless you have numbers stored as strings.
teams.sort()
print('Teams after sorting:', teams)
print('---------------------------------------------------------------------')

# When you want to delete an item at a particular index, you can
# use the del keyword. Python will automatically move the other
# items in to fill the index vacated after your delete so there
# are no holes in the list.
deleted_team = teams[7]
del teams[7]
print('You deleted', deleted_team, 'position 7 is now', teams[7])
print('---------------------------------------------------------------------')

# Sometimes, you want to know what position an item is in.
# You can use the .index method to find that. You will have to use
# the try / except block. We'll learn about what that means later.
try:
  search = input('Enter a team to search for: ')
  found_at = teams.index(search)
  print(search, 'was found at position', found_at)
except ValueError:
  print(search, 'was not found')
print('---------------------------------------------------------------------')

# The .remove method works the same as .index, except it removes
# the item from the list if it finds it instead of returning it.
try:
  search = input('Enter a team to remove: ')
  teams.remove(search)
  print(search, 'was removed')
except ValueError:
  print(search, 'was not found')
print('---------------------------------------------------------------------')

# Finally, min and max are Python built-in functions that can return
# the smallest and largest items from a sequence respectively.
print('The lowest team name is', min(teams))
print('The highest team name is', max(teams))

