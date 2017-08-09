#!/usr/bin/python3

# set1 will be the even numbers from 1-20 (yes, you can use range to build sets)
set1 = set(range(2, 21, 2))
# set2 will be the multiples of 3 from 1-30
set2 = set(range(0, 31, 3))
set2.add(1)
set2.remove(0)

print('set1=', set1)
print('set2=', set2)

print('====================  Union ====================')
print('Union of set1 and set2', set1.union(set2), sep='\n\t')
print('Union of set1 and set2 using | syntax', set1 | set2, sep='\n\t')

print('====================  Intersection ====================')
print('Intersection of set1 and set2', set1.intersection(set2), sep='\n\t')
print('Intersection of set1 and set2 using & syntax', set1 & set2, sep='\n\t')

print('====================  Difference ====================')
print('Difference of set1 and set2', set1.difference(set2), sep='\n\t')
print('Difference of set1 and set2 using - syntax', set1 - set2, sep='\n\t')

print('====================  Subset ====================')
sub = set([2, 4, 6])
print('set(2, 4, 6) subset of set1?', sub.issubset(set1), sep='\n\t')
print('set(2, 4, 6) subset of set1 using <= syntax?', sub <= set1, sep='\n\t')

print('====================  Superset ====================')
print('set1 superset of set(2, 4, 6)?', set1.issuperset(sub), sep='\n\t')
print('set1 superset of set(2, 4, 6) using >= syntax?', set1 >= sub, sep='\n\t')
