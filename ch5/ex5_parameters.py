#!/usr/bin/python3

def main():
    double_me(2)
    double_me(4)
    double_me(128)

def double_me(value):
    # value is a formal parameter. That means that value can be used
    # just like a local variable inside of this function.
    print('I was {}, but now I am {}'.format(value, value * 2))
    
main()
