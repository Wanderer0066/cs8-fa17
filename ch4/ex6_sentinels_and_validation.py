#!/usr/bin/python3

# Our sentinel value will be 0. When the user requests 0 shares we'll terminate.
SENTINEL = 'DONE'  # Note that we capitalized it since it's a module variable

# Our main function will call our other functions to accumulate a running sum
# of stock shares.
def main():
    purchased = 0
    shares = input('How many shares do you want? ')
    while shares != SENTINEL:
        purchased += validate_shares(shares)
        shares = input('How many shares do you want this time? ')
    print('You purchased {} shares total'.format(purchased))
    
    
# Our validation function will accept a shares parameter and will stay in loop
# until the shares provided by the user are within the acceptable boundaries.
# Then, we'll return a the shares variable to our caller.
def validate_shares(shares):
    while not shares.isdigit() or int(shares) < 5 or int(shares) > 100:
        print('You must purchase between 5 and 100 shares')
        shares = input('Now, try this again. How many do you want? ')
    return int(shares)
    
main()
