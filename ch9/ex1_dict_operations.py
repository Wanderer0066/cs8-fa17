#!/usr/bin/python3

# Below, we create a new dict object and assign the name and  major keys to
# their initial values
student = {'name': 'Sally Student', 'major': 'Computer Science'}

# We can also create an empty dict object and assign its keys using the
# square-bracket syntax we are familiar with from lists. Remember that with
# dicts, keys can be any immutable type (even tuples can be keys) unlike lists
# where indices are always numeric.
student2 = {}
student2['name'] = 'Joe Cool'
student2['major'] = 'Mathematics'

# Dicts are mutable just like lists, so we can access a key's value by name and
# read/modify it, or add new keys.
student['gpa'] = 2.75
student2['gpa'] = 3.33
student2['major'] = 'Psychology'

# Notice that when we print dict objects, the keys do not appear in the same
# order as we added it. This is because keys are not sequence objects. Python
# optimizes how the data is stored in them so you cannot and should not rely
# on key ordering.
print('Student', student)
print('Student2', student2)
