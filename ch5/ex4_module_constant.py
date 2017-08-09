#!/usr/bin/python3

# MY_CONSTANT is visible anywhere within this file (module)
MY_CONSTANT = 'Jason'
CALC_FACTOR = 1.5

def main():
    print('I can use MY_CONSTANT here', MY_CONSTANT)
    inner_function('Some junk')
    number = int(input('Multiply by: '))
    print('{} * {} = {}'.format(number, CALC_FACTOR,
        number * CALC_FACTOR))
    
def inner_function(other_text):
    CALC_FACTOR = 7.0
    print('I can also use it here', MY_CONSTANT, 'with', other_text)
    

main()
print('I can also use it at the module scope', MY_CONSTANT)
