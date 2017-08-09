#!/usr/bin/python3

def main():
    print('First employee')
    calculate_payroll()
    print('Second employee')
    calculate_payroll()
    print('Third employee')
    calculate_payroll()


def calculate_payroll():
    employee = input('Enter employee name: ')
    hours_worked = int(input('Enter hours worked: '))
    hourly_rate = float(input('Enter hourly rate: '))
    overtime = 0
  
    pay = 0
    if hours_worked <= 40:
        pay = hours_worked * hourly_rate
    else:
        overtime = hours_worked - 40
        pay = 40 * hourly_rate
        pay += overtime * hourly_rate * 1.5

    print('{}: {} hours, ${:.2f}'.format(employee, hours_worked, pay))
    if overtime:
        print('{} hours of overtime'.format(overtime))

# Here's where we will call the main function
main()
