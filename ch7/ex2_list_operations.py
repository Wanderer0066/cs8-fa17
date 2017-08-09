#!/usr/bin/python3

# This is a basic list containing integers
list1 = [1, 3, 5, 11]

# Lists can also contain strings, or can mix types
list2 = [1, 'abc', 'efg', 3.5]

# Let's add list1 and list2 together
list3 = list1 + list2

# The * operator repeats the items in a list the specified
# number of times. The following statements will create 10
# zeroes in list4
list4 = [0]
list4 = list4 * 10

print('list3=', list3)
print('list4=', list4)

# Lists are indexed by using the name of the list variable
# followed by the index to access inside of square brackets.
# Remember, list indices start at 0 and not 1!
print('The 2nd item in list3 is', list3[1])
print('The last item in list4 is', list4[9])

# The in operator can be used to determine if an item
# is found in a list. This can be part of a condition statement.
if 'abc' in list3:
  print('I found abc in the list')

if 100 in list3:
  print('I found 100 in the list')
else:
  print('100 was not found')
