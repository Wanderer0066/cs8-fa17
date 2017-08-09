#!/usr/bin/python3

# Lists of values for for loops do not need to be numbers or in increasing
# order. Name is the variable being used to iterate over the list of Beatles.
for name in ['John', 'Paul', 'George', 'Ringo']:
    print('{} was in a famous band!'.format(name))
    

# Loops make it really easy to do summarization of data, such as calculating
# a sum or average.
total = 0
count = 0
for score in [78, 81, 93, 94, 87, 68]:
    total += score
    count += 1
# Remember, once the loop has completed, execution continues at the next
# statement
print('Avg Score on {} tests = {}'.format(count, total / count))
