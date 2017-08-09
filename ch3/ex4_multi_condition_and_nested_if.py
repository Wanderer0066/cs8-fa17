#!/usr/bin/python3

years_of_experience = int(input('Enter years of experience: '))
degree = input('Enter the highest degree earned: ')

if years_of_experience > 0 and years_of_experience < 3:
    salary = 35000
elif years_of_experience >= 3 and years_of_experience < 7:
    salary = 45000
elif years_of_experience >= 7 and years_of_experience < 10:
    salary = 55000
elif years_of_experience >= 10:
    salary = 65000
    if degree == 'Masters' or degree == 'Doctorate':
       salary += 10000

print('Your salary is ${:,.2f}'.format(salary))

  
