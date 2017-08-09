#!/usr/bin/python3

def main():
    multiply_me(2, 10)
    multiply_me(4, 16)
    multiply_me(128, 128)

def multiply_me(value, multiplier):
    print('{} x {} = {}'.format(value, multiplier, value * multiplier))
    
main()
