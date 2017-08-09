#!/usr/bin/python3

# This is a basic list containing integers
list1 = [1, 3, 5, 11]

# Lists can also contain strings, or can mix types
list2 = [1, 'abc', 'efg', 3.5]

# Let's add list1 and list2 together
list3 = list1 + list2

# The len function returns the length of a list.
print('list3 has', len(list3), 'items')
# We can use it to loop over each list index.
for i in range(len(list3)):
  print('i={}, list3[{}]={}'.format(i, i, list3[i]))

print('---------------------------------------------------------------------')
# We can also loop directly over the items of a list
# Notice how in the previous case, i iterated through the
# index values from 0 to len(list3) - 1. Here i will
# iterate through the values in list3.
for i in list3:
  print('i={}'.format(i))

