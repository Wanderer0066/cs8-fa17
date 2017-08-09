#!/usr/bin/python3

# Here, I am telling Python to make the random module available to me
import random

def main():
    print('This is a simple coin flip simulator')
    print('Flip 1')
    flip()
    print('Flip 2')
    flip()
    print('Flip 3')
    flip()
    
def flip():
    # random.randint will return an int in the range
    # specified by the parameters.
    if random.randint(1, 100) <= 50:
        print('Heads! I win')
    else:
        print('Tails! You lose')

main()
