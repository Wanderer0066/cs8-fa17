#!/usr/bin/python3

income = int(input('What is your monthly income? '))
debt = int(input('How much are your monthly bills? '))
loan_amt = float(input('How much do you want to borrow? '))

monthly_payment = loan_amt / 36  # 3 year loan

# Check if buyer has enough income to cover new payment
if income - debt < monthly_payment:
  print('Sorry, {:,.2f} - {:,.2f} is not enough to cover your loan payment of {:,.2f}'.format(
        income, debt, monthly_payment))
else:
  # debt to income ratio must be less than 1:1.5
  debt_to_income = (debt + monthly_payment) / income
  if debt_to_income <= 0.667:
    print('Congratulations, you are approved with a payment of {:,.2f}'.format(monthly_payment))
  else:
    print('Sorry, your debt-to-income ration of {:,.2%} is too high'.format(debt_to_income))


