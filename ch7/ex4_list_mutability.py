#!/usr/bin/python3

# Build a list counting from 1 to 20
list1 = list(range(1, 21))
# You can access members of a list by index.
first = list1[0]

# Negative indices count backwards from the end position.
# -1 will be the last element
last = list1[-1]
# -len will be the first element, same as list1[0]
first2 = list1[-20]

# Remember, since indices start at 0, the 10th element is index 9.
# When you use negative indices, you count backwards from length
# so 20 - 11 is 9.
same = list1[9] == list1[-11]

print('first=', first)
print('last=', last)
print('first2=', first2)
print('same?', same)

# We can change a list's values by accessing its items by index.
# Here, we do it in a loop.
for i in range(len(list1)):
  list1[i] *= 2  # We're going to double each item in the list

print('After for loop over indices list1=', list1)


# Why doesn't this work? Because when a for loop is iterated over
# directly, the loop variable gets a copy of the actual item and not
# access to the original list member. i is just a local variable
# that cannot change the item in list1 that it is a copy of.
for i in list1:
  i *= 2

print('After for loop list1=', list1)
