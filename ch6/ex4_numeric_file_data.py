#!/usr/bin/python3

f = open('ex4_salaries.txt')

# We'll store each salary value in a list
salaries = []

# Here's a another common technique for file processing. Our while loop
# will always evaluate to True which would normally be an infinite loop.
# However, inside of the loop we'll evaluate the line that we read and
# do an explicit break statement if its empty
while True:
    line = f.readline().strip()
    # Here we check that line contains digits. If so, we add it to the list.
    # Otherwise, we break the loop.
    if line.isnumeric():
        salaries.append(int(line))
    else:
        break

print('Read', len(salaries), 'from file')
print('Max {}, Min {}, Total {}'.format(
    max(salaries), min(salaries), sum(salaries)))
