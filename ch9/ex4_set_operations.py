#!/usr/bin/python3

# Let's build a set from a list.
grades = set(['A', 'B', 'C', 'D', 'F'])
print('grades=', grades)

print('====================  .add() ====================')
grades.add('A-')
grades.add('B+')
# Notice that if we try to add an item that already exists, no exception occurs,
# but the item is not duplicated
grades.add('A')
print('\tgrades=', grades)

print('====================  .update() ====================')
# Update lets us add multiple items from a sequence in one operation
grades.update(['B-', 'C+', 'C-', 'D+', 'D-'])
print('\tgrades=', grades)

print('====================  .remove() ====================')
# .remove can remove an item, but only if it exists
grades.remove('D-')
print('\tgrades=', grades)

print('====================  in/not in ====================')
# Sets are efficient data structures for keeping track of unique lists. The in
# and not in operators let you know if something is found in your set.
print('"a" in grades?', 'a' in grades)
print('"a" not in grades?', 'a' not in grades)

print('====================  For loop ====================')
# Remember, just like with dict keys, the items in a set are unordered so you
# cannot rely on any type of ordering to be consistent in your program.
for g in grades:
  print('Grade:', g)
