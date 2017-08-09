#!/usr/bin/python3

def calculate_loan_amount(principle, rate=0.0625, years=3):
    compound_amt = principle * (1 + rate / 12) ** (12 * years)
    out = (
        'The full amount paid on ${:,.2f} at {:,.2%} for {} years '
        'is ${:,.2f}')
    print(out.format(principle, rate, years, compound_amt))

def main():
    calculate_loan_amount(10000)  # Defaults will be used
    calculate_loan_amount(10000, 0.08)  # Specify rate 
    calculate_loan_amount(10000, 0.08, 5)  # Specify all
    calculate_loan_amount(10000, years=5)
    # This will not work, named arguments must be after positional
    #calculate_loan_payments(10000, years=5, 0.08)
    
main()
