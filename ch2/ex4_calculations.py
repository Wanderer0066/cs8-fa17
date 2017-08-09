#!/usr/bin/python3

# Remeber the order of operations
a = 10 + 24 * 15
b = (10 + 24) * 15
c = 2 ** 10
print('a=', a, 'b=', b, 'c=', c)

# In Python3, floating point division is the default
d = 25 / 4
# In Python2, integer division is the default
# Use the // operator to force integer division in Python3
d2 = 25 // 4
# The % operator returns the modulus, or remainder of a division operation
r = 25 % 4
print('d=', d, 'd2=', d2, 'r=', r)
