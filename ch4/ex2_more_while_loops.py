#!/usr/bin/python3

# Notice that the loop below will never print anything because its conditional
# statement will always resolve to False.
day = 'Saturday'
while day == 'Tuesday' or day == 'Thursday':
    print('Go to CS008 class!')
    
    
# This is an infinite loop! There is nothing inside of the loop's body that will
# ever change the value of day so the only way to kill this program is to hit 
# Ctrl-C and terminate the Python interpreter.
while day == 'Saturday':
    print('Sleep it off!')
