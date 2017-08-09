#!/usr/bin/python3

def main():
    multiply_me(2, 10)
    multiply_me(4, 16)
    multiply_me(128, 128)
    value = 100
    multiply_me(value, 5)
    print('Notice that I did not change', value)
    

def multiply_me(value, multiplier):
    print('{} x {} = {}'.format(value, multiplier, value * multiplier))
    value = 0  # This statement has no effect outside of the function
    print('Inside of the function, value =', value)
    
main()
